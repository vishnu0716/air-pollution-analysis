

import pandas as pd
import numpy as np
from scipy import stats

# =========================
# LOAD DATA
# =========================
file_path = "air pollution.csv"

try:
    df = pd.read_csv(file_path)
except:
    df = pd.read_csv(file_path, sep=';')

# =========================
# DATA CLEANING
# =========================
df.columns = df.columns.str.strip().str.lower()

df['pollutant_avg'] = pd.to_numeric(df['pollutant_avg'], errors='coerce')
df['pollutant_min'] = pd.to_numeric(df['pollutant_min'], errors='coerce')
df['pollutant_max'] = pd.to_numeric(df['pollutant_max'], errors='coerce')

df = df.dropna()

print("✅ Data Loaded Successfully")

# =========================
# STATISTICAL TESTING
# =========================
data = df['pollutant_avg']

# Z-Test (manual)
z_score = (np.mean(data) - 50) / (np.std(data) / np.sqrt(len(data)))

# T-Test
t_stat, p_val = stats.ttest_1samp(data, 50)

# Shapiro Test (Normality)
sample = data.sample(min(500, len(data)))  # safe sampling
s_stat, s_p = stats.shapiro(sample)

# =========================
# OUTPUT RESULTS
# =========================
print("\n================ STATISTICAL TESTS ==========\n")

print(f"Z-score       : {z_score:.4f}")
print(f"T-test        : {t_stat:.4f}, p-value: {p_val:.4e}")
print(f"Shapiro Test  : {s_stat:.4f}, p-value: {s_p:.4e}")

# =========================
# INTERPRETATION (IMPORTANT)
# =========================
print("\n================ INTERPRETATION =============\n")

if p_val < 0.05:
    print("T-Test: Significant difference from mean (50)")
else:
    print("T-Test: No significant difference from mean (50)")

if s_p < 0.05:
    print("Shapiro Test: Data is NOT normally distributed")
else:
    print("Shapiro Test: Data is normally distributed")

print("\n✅ Statistical testing completed")