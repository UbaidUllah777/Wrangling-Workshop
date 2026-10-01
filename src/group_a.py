import pandas as pd


class MissingValueHandler:
    def handle(self, df):
        df = df.copy()

        # Treat blank text as missing
        df = df.replace(r"^\s*$", pd.NA, regex=True)

        # Fill missing descriptive text
        for column in ["Name", "Skills", "Topic"]:
            df[column] = df[column].fillna("Unknown")

        # Keep missing assessment IDs and scores:
        # no assessment does not mean a score of zero.

        print("\nMissing values after handling:")
        print(df.isna().sum())

        return df