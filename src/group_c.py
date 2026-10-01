import pandas as pd


class FeatureEngineer:
    def create_features(self, df):
        df = df.copy()
        experience = df["Years of Experience"]

        # More than 3 years means experienced.
        # Missing experience remains unknown.
        df["Experienced"] = (
            experience.gt(3)
            .astype("boolean")
            .mask(experience.isna(), pd.NA)
        )

        # Categories defined for this exercise
        df["Experience Level"] = pd.cut(
            experience,
            bins=[0, 2, 5, float("inf")],
            labels=["Junior", "Mid-level", "Senior"],
            include_lowest=True
        )

        # Track assessment and score availability separately
        df["Has Assessment"] = df["AssessmentID"].notna()
        df["Has Score"] = df["Assessment Score"].notna()

        print("\nNew features:")
        print(df[
            [
                "CandidateID",
                "Experienced",
                "Experience Level",
                "Has Assessment",
                "Has Score"
            ]
        ].head())

        return df