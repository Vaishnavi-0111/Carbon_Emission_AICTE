# 🌍 Carbon Emissions Prediction

**AICTE Internship – June 2025**
**Hosted by:** Shell x Edunet Foundation – Skills4Future
**Intern:** *Vaishnavi Kadam*

---

## 📘 Project Overview

This project aims to predict **carbon emissions** for various countries using machine learning models trained on historical emissions data. It was developed during the AICTE Virtual Internship Program (June–July 2025) under the mentorship of **Raghunandan M S**.

---

## 🎯 Objective

To build a predictive model that estimates carbon emissions based on multiple features like cereal yield, GNI per capita, Energy per capita, urban population, protected area, population growth rate and urban population growth rate, using real-world datasets.

---

## 🧠 Skills Applied

* Regression Modeling
* Data Cleaning & Preprocessing
* Exploratory Data Analysis (EDA)
* Model Evaluation (R², RMSE)
* Visualization with Matplotlib & Seaborn
* Tools: Python, Pandas, Scikit-learn, Jupyter Notebooks, Streamlit

---

## 🗂️ Project Structure

```
Carbon_Emission_AICTE/
│
├── Week1/                # Data cleaning & exploration
├── Week2/                # Feature engineering & EDA
├── Week3/                # Model training & evaluation
├── dataset/              # Raw and cleaned datasets
├── model_results/        # Graphs, metrics, final model
├── app.py                # Streamlit app for deployment
└── README.md             # Project overview
```

---

## 📊 Data Description

* **Source:** Provided during internship
* **Features:** Country, Year, CO₂ Emissions, Energy Use, GDP, Population
* **Target Variable:** Carbon Emissions (in metric tons)

---

## 🚀 Deployment

The model has been deployed locally using **Streamlit** for interactive predictions and visualizations.

### ▶️ How to Run the Streamlit App Locally

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

3. The app will launch in your browser at:

   ```
   http://localhost:8501
   ```

### 🧩 Streamlit App Features

* Input prediction features manually or via file upload
* Visualize historical trends and country-specific emissions
* View model predictions and performance metrics

---

## ✅ Results

* **Model Used:** (e.g. Linear Regression / Random Forest Regressor)
* **Performance Metrics:**

  * R² Score: `0.92` *(replace with your result)*
  * RMSE: `15.3`
* **Key Insight:** GDP and Energy Use were the most influential factors

---

## 📈 Future Scope

* Add real-time data integration
* Deploy app online via Streamlit Cloud
* Expand to include methane, nitrous oxide predictions

---

## 📩 Contact

**Trainer:** Raghunandan M S
**Organization:** Edunet Foundation – Skills4Future
**Intern:** *Vaishnavi Kadam*
