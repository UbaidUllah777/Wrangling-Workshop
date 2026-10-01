import pandas as pd


class DataCleaner:
    def clean(self, df):
        df = df.copy()

        # Clean extra spaces in text
        for column in ["Name", "Skills", "AssessmentID", "Topic"]:
            df[column] = (
                df[column]
                .astype("string")
                .str.strip()
                .str.replace(r"\s+", " ", regex=True)
            )

        # Convert numeric columns; invalid values become missing
        for column in ["Years of Experience", "Assessment Score"]:
            df[column] = pd.to_numeric(df[column], errors="coerce")

        # Negative experience is invalid
        df.loc[
            df["Years of Experience"] < 0,
            "Years of Experience"
        ] = float("nan")

        # Remove identical rows, keeping distinct assessments
        original_count = len(df)
        df = df.drop_duplicates().copy()

        print(f"\nDuplicates removed: {original_count - len(df)}")
        print("\nData types after cleaning:")
        print(df.dtypes)

        return df