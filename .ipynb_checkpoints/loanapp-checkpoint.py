# import required libraries
import joblib
import streamlit as st
import numpy as np
import json
import datetime

with open("min_max_dict.json","r") as f:
    min_max_dict = json.load(f)

model = joblib.load("RandomForest.pkl")

# App title
st.set_page_config(page_title="Loan Defaulter Prediction App", layout="centered")
st.title("💰 Loan Defaulter Prediction App")
st.markdown("Enter the following details to predict if a person has payment difficulties:")

st.divider()
gender_options = {"M":1,"F":0}
NameIncomeType = {'Businessman':0,
                  'Commercial associate':1,
                  'Maternity leave':2,
                  'Pensioner':3,
                  'State servant':4,
                  'Student':5,
                  'Unemployed':6,
                  'Working':7}
NameEducationType = {'Academic degree':0,
                    'Higher education':1, 
                    'Incomplete higher':2,
                    'Lower secondary':3,
                    'Secondary / secondary special':4}

# Create input form with columns
col1, col2 = st.columns(2,border = True)

with col1:
    with st.container(border = True):
        gender = st.radio("**GENDER**",options =list(gender_options.keys()),horizontal = True)
        gender_value = gender_options[gender]
    
    with st.container(border = True):
        dateofbirth = st.date_input("**DATE OF BIRTH**",value = datetime.date(1990,12,1),
                                    format = "DD/MM/YYYY", 
                                    min_value = datetime.date(1990,12,1),
                                   max_value = datetime.date(2025,12,31))
        today = datetime.date.today()
        daysold = (dateofbirth - today).days
    
    with st.container(border = True):
        credit = st.slider("**SELECT AMOUNT**",
                       min_value =min_max_dict["AMT_GOODS_PRICE"]["min"],
                       max_value = min_max_dict["AMT_GOODS_PRICE"]["max"],
                       value = min_max_dict["AMT_GOODS_PRICE"]["min"],
                       step = float(1000))
    
    with st.container(border = True):
        incometype = st.selectbox("**SELECT INCOME TYPE**",options = list(NameIncomeType.keys()))
        incomevalue = (NameIncomeType[incometype])
    
    with st.container(border = True):
        educationlevel = st.selectbox("**SELECT EDUCATION LEVEL**", options = list(NameEducationType.keys()))
        educationvalue = NameEducationType[educationlevel]
   
        
with col2:
    with st.container(border = True):
        jobold = st.slider("**DAYS EMPLOYED**",
                       min_value =min_max_dict["DAYS_EMPLOYED"]["min"],
                       max_value = min_max_dict["DAYS_EMPLOYED"]["max"],
                       value = min_max_dict["DAYS_EMPLOYED"]["min"])
    with st.container(border = True):
        idold = st.slider("**DAYS ID PUBLISH**",
                       min_value =min_max_dict["DAYS_ID_PUBLISH"]["min"],
                       max_value = min_max_dict["DAYS_ID_PUBLISH"]["max"],
                       value = min_max_dict["DAYS_ID_PUBLISH"]["min"])
    with st.container(border = True):
            extsource2 = st.slider("**EXT_SOURCE_2**",
                       min_value =min_max_dict["EXT_SOURCE_2"]["min"],
                       max_value = min_max_dict["EXT_SOURCE_2"]["max"],
                       value = min_max_dict["EXT_SOURCE_2"]["min"])
    with st.container(border = True):
        phoneold = st.slider("**DAYS_LAST_PHONE_CHANGE**",
                       min_value =min_max_dict["DAYS_LAST_PHONE_CHANGE"]["min"],
                       max_value = min_max_dict["DAYS_LAST_PHONE_CHANGE"]["max"],
                       value = min_max_dict["DAYS_LAST_PHONE_CHANGE"]["min"])
    with st.container(border = True):
        docflag = st.slider("**FLAG_DOCUMENT_3**",
                       min_value =min_max_dict["FLAG_DOCUMENT_3"]["min"],
                       max_value = min_max_dict["FLAG_DOCUMENT_3"]["max"],
                       value = min_max_dict["FLAG_DOCUMENT_3"]["min"])
            
    

# Prepare input for model
# Prepare input for model
input_array = np.array([[gender_value, credit, incomevalue, educationvalue,
                         daysold, jobold, idold, extsource2, phoneold, docflag]])

st.write("Input Array:", input_array)

# Make prediction when user clicks button
if st.button("🔮 Predict"):
    try:
        prediction = model.predict(input_array)[0]   # 0 or 1 (No default / Default)
        probability = model.predict_proba(input_array)[0][1]  # probability of default

        if prediction == 1:
            st.error(f"⚠️ The model predicts that this person is **likely to default** "
                     f"(Probability: {probability:.2f})")
        else:
            st.success(f"✅ The model predicts that this person is **not likely to default** "
                       f"(Probability of default: {probability:.2f})")

    except Exception as e:
        st.error(f"Error during prediction: {e}")