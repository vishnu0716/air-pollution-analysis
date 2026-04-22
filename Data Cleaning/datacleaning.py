
import pandas as pd

# Load dataset
file_path = "air pollution.csv"

try:
    df = pd.read_csv(file_path)
except:
    df = pd.read_csv(file_path, sep=';')

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Convert columns to numeric
df['pollutant_min'] = pd.to_numeric(df['pollutant_min'], errors='coerce')
df['pollutant_max'] = pd.to_numeric(df['pollutant_max'], errors='coerce')
df['pollutant_avg'] = pd.to_numeric(df['pollutant_avg'], errors='coerce')

# Remove missing values
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned data
df.to_csv("cleaned_air_pollution.csv", index=False)

print("Data cleaning completed successfully")