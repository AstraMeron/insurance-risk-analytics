# 1. Import the Pandas library
import pandas as pd

# Define the file path (since it's in the same directory, the filename is enough)
DATA_FILE = "MachineLearningRating_v3"

# 2. Load the data
# We assume it's comma-separated (CSV). If it doesn't work, we'll try sep='\t' (tab)
try:
    df = pd.read_csv(DATA_FILE)
    print("Data loaded successfully!")
    print("\n--- First 5 Rows ---")
    print(df.head())
    print("\n--- Data Information ---")
    df.info()
except Exception as e:
    print(f"Failed to load data. The separator might be incorrect: {e}")

# IMPORTANT: Check the output of df.head() to see if the columns look correct.