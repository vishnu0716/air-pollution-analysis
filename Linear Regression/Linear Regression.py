
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

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

df['pollutant_min'] = pd.to_numeric(df['pollutant_min'], errors='coerce')
df['pollutant_max'] = pd.to_numeric(df['pollutant_max'], errors='coerce')
df['pollutant_avg'] = pd.to_numeric(df['pollutant_avg'], errors='coerce')

df = df.dropna()

print("✅ Data Loaded Successfully")

# =========================
# FEATURE SELECTION
# =========================
X = df[['pollutant_min', 'pollutant_max']]
y = df['pollutant_avg']

# =========================
# TRAIN-TEST SPLIT
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# MODEL TRAINING
# =========================
model = LinearRegression()
model.fit(X_train, y_train)

# =========================
# PREDICTIONS
# =========================
predictions = model.predict(X_test)

# =========================
# MODEL EVALUATION
# =========================
r2 = r2_score(y_test, predictions)

print("\n================ MODEL PERFORMANCE ==========\n")
print(f"R2 Score : {r2:.4f}")

# =========================
# MODEL COEFFICIENTS (INSIGHT)
# =========================
print("\n================ MODEL INSIGHTS =============\n")
print(f"Intercept       : {model.intercept_:.4f}")
print(f"Coefficient Min : {model.coef_[0]:.4f}")
print(f"Coefficient Max : {model.coef_[1]:.4f}")

print("\n✅ Machine learning model completed")