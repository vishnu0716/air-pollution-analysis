

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
# BASIC INFO
# =========================
print("\n📊 Dataset Preview:\n")
print(df.head().to_string(index=False))

print("\n📈 Dataset Info:")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\n📊 Summary Statistics:\n")
print(df[['pollutant_min','pollutant_max','pollutant_avg']].describe())

# =========================
# 1. HISTOGRAM
# =========================
plt.figure()
plt.hist(df['pollutant_avg'], bins=30)
plt.title("Pollution Distribution")
plt.savefig("histogram.png")
plt.show()

# =========================
# 2. BOX PLOT
# =========================
plt.figure()
plt.boxplot(df['pollutant_avg'])
plt.title("Outlier Detection")
plt.savefig("boxplot.png")
plt.show()

# =========================
# 3. SCATTER PLOT
# =========================
plt.figure()
plt.scatter(df['pollutant_min'], df['pollutant_max'])
plt.title("Min vs Max Pollution")
plt.xlabel("Min")
plt.ylabel("Max")
plt.savefig("scatter.png")
plt.show()

# =========================
# 4. HEATMAP
# =========================
plt.figure()
sns.heatmap(df[['pollutant_min','pollutant_max','pollutant_avg']].corr(), annot=True)
plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")
plt.show()

# =========================
# 5. BAR CHART
# =========================
city_avg = df.groupby('city')['pollutant_avg'].mean().head(10)

plt.figure()
city_avg.plot(kind='bar')
plt.title("Top Cities Pollution")
plt.savefig("bar_chart.png")
plt.show()

# =========================
# 6. PIE CHART
# =========================
plt.figure()
plt.pie(city_avg, labels=city_avg.index, autopct='%1.1f%%')
plt.title("City Pollution Share")
plt.savefig("pie_chart.png")
plt.show()

# =========================
# 7. VIOLIN PLOT
# =========================
plt.figure()
sns.violinplot(y=df['pollutant_avg'])
plt.title("Pollution Distribution Shape")
plt.savefig("violin.png")
plt.show()

# =========================
# 8. PAIRPLOT
# =========================
sns.pairplot(df[['pollutant_min','pollutant_max','pollutant_avg']])
plt.savefig("pairplot.png")
plt.show()

# =========================
# 9. LINE PLOT
# =========================
df_sorted = df.sort_values('pollutant_avg').reset_index(drop=True)
df_sorted['sequence'] = range(len(df_sorted))

plt.figure()
plt.plot(df_sorted['sequence'], df_sorted['pollutant_avg'])
plt.title("Pollution Trend (Ordered Data)")
plt.xlabel("Observations")
plt.ylabel("Pollution Avg")
plt.savefig("line_plot.png")
plt.show()

print("\n✅ EDA completed successfully")