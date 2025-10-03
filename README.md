# 💰 Loan Defaulter Prediction Project

This project aims to predict whether a loan applicant is likely to default on their payments using machine learning. The workflow covers **data exploration (EDA)**, **model building**, and deployment as a **Streamlit web application**.

---

## 📂 Project Structure

* **MLProject_ccdata.ipynb**
  Jupyter Notebook containing exploratory data analysis (EDA), feature engineering, and model building steps.

* **RandomForest.pkl**
  Trained Random Forest model saved using `joblib`.

* **min_max_dict.json**
  A JSON file storing minimum and maximum values of features (used to set slider ranges in the app).

* **app.py**
  Streamlit web application for loan default prediction.

---

## 🔍 Exploratory Data Analysis (EDA)

The notebook (`MLProject_ccdata.ipynb`) includes:

* Data cleaning and preprocessing
* Handling categorical variables (encoding)
* Exploratory data analysis (distribution of features, correlation analysis)
* Feature engineering (e.g., age calculation, employment duration)
* Train-test split and model evaluation

---

## 🤖 Model Building

* **Algorithm Used:** Random Forest Classifier
* **Evaluation Metrics:** Accuracy, Precision, Recall, ROC-AUC
* **Output:** Model serialized and saved as `RandomForest.pkl`

---

## 🌐 Streamlit Web Application

The app (`app.py`) provides a user-friendly interface for predicting loan default.

### Features:

* Collects user input (gender, income type, education, employment days, etc.)
* Uses sliders and dropdowns for easy interaction
* Converts categorical inputs into numerical codes
* Prepares input array and passes it to the trained Random Forest model
* Displays prediction with probability

### Input Fields:

* Gender
* Date of Birth (used to calculate age in days)
* Credit Amount (`AMT_GOODS_PRICE`)
* Income Type
* Education Level
* Days Employed
* Days ID Published
* EXT_SOURCE_2
* Days Last Phone Change
* Flag Document 3

---

## 🚀 How to Run the Project

1. Clone the repository or copy project files into a folder.

2. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   **requirements.txt** should include:

   ```
   streamlit
   joblib
   numpy
   pandas
   scikit-learn
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

4. Open the app in your browser at `http://localhost:8501`

---

## 📊 Prediction Output

* **✅ Not likely to default**: If the model predicts no payment difficulties.
* **⚠️ Likely to default**: If the model predicts potential payment difficulties.

The app also shows the **probability score** for transparency.

---
