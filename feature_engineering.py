from sklearn.base import BaseEstimator, TransformerMixin

class FeatureEngineering(BaseEstimator, TransformerMixin):
    def fit(self, x, y=None):
        return self

    def transform(self, x):
        x = x.copy()

        # education mapping
        edu_map = {"High School": 0,
           "Diploma": 1,
           "Bachelor": 2,
           "Master": 3,
           "PhD": 4}

        # Location mapping
        loc_map = {"USA": 9,
                   "Canada": 8,
                   "UK": 7,
                   "Germany": 6,
                   "Remote": 5,
                   "Sweden": 4,
                   "Australia": 3,
                   "Singapore": 2,
                   "Netherlands": 1,
                   "India": 0}
        
        # company mapping
        company_map = {"Startup": 0,
               "Small": 1,
               "Medium": 2,
               "Large": 3,
               "Enterprise": 4}

        # total experience
        x["education_year"] = x["education_level"].map(edu_map)
        x["total_experience"] = (x["experience_years"] + x["education_year"])

        # company-size-location feature
        x["loc_level"] = x["location"].map(loc_map)
        x["comp"] = x["company_size"].map(company_map)

        x["comp_size_loc"] = (x["loc_level"] + x["comp"])

        # remove temporary columns
        x.drop(columns=["loc_level","comp","education_year"], axis=1, inplace=True)

        return x