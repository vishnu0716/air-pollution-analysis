# 🌍 Air Pollution Data Analysis & Visualization

This project performs **data analysis, visualization, statistical testing, and machine learning** on an air pollution dataset using Python.

---

## 📌 Project Overview

The objective of this project is to analyze air pollution data and extract meaningful insights using data science techniques.

The project includes:

* Data preprocessing and cleaning
* Exploratory Data Analysis (EDA)
* Data visualization using multiple plots
* Statistical hypothesis testing
* Machine learning model for prediction

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SciPy
* Scikit-learn

---

## 📂 Dataset

The dataset taken from : https://www.data.gov.in/

**File Name:** `air pollution.csv`

### Required Columns:

* `city`
* `pollutant_min`
* `pollutant_max`
* `pollutant_avg`

---

## ⚙️ Data Preprocessing

The following steps are performed:

* Load dataset from CSV file
* Handle different delimiters
* Clean column names (lowercase, remove spaces)
* Convert columns to numeric values
* Remove missing/null values

---

## 📊 Data Visualization

The project generates the following visualizations:

1. **Histogram** – Shows distribution of pollution levels
2. **Box Plot** – Detects outliers
3. **Scatter Plot** – Relationship between min and max pollution
4. **Heatmap** – Correlation between variables
5. **Bar Chart** – Top polluted cities
6. **Pie Chart** – Contribution of cities to pollution
7. **Violin Plot** – Distribution shape of pollution
8. **Pairplot** – Relationships between all variables
9. **Line Plot** – Trend of pollution values

All plots are automatically saved as `.png` files.

---

## 📈 Statistical Analysis

The project includes:

* **Z-Test** → Checks deviation from mean value (50)
* **T-Test (One Sample)** → Compares sample mean with population mean
* **Shapiro Test** → Tests normality of data

---

## 🤖 Machine Learning Model

A **Linear Regression model** is used to predict pollution levels.

### Input Features:

* pollutant_min
* pollutant_max

### Target:

* pollutant_avg

### Model Evaluation:

* R² Score (accuracy metric)

---

## ▶️ How to Run the Project

### Step 1: Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scipy scikit-learn
```

### Step 2: Place Dataset

Put `air pollution.csv` in the project folder.

### Step 3: Run the Script

```bash
python your_script_name.py
```

---

## 📤 Output

The project generates:

* Graph images (`.png` files)
* Statistical test results (console output)
* Dataset summary and insights
* Model performance (R² score)

---

## 📌 Sample Outputs

* Dataset preview
* Summary statistics
* Hypothesis testing results
* Model accuracy

---

## 🚀 Future Enhancements

* Add time-series analysis
* Include more pollution parameters
* Improve model using advanced algorithms
* Build interactive dashboard (Power BI / Streamlit)
* Deploy as a web application

---

## 📁 Project Structure

```
📦 Air-Pollution-Analysis
 ┣ 📜 air pollution.csv
 ┣ 📜 analysis.py
 ┣ 📜 README.md
 ┣ 📂 outputs (images)
```

---

## 👨‍💻 Author

Pulikanti Vishnuvardhan Reddy
B.Tech Student | Data Science Enthusiast

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!
