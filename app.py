import streamlit as st
import joblib
import pandas as pd
st.set_page_config(
    page_title="Bank Loan Repayment Analysis and Customer Risk Assessment",
    page_icon="favicon.ico",
    layout="wide"
)
st.markdown("""
<h1 style='text-align:center;color:#1E88E5;'>Bank Loan Repayment Analysis and Customer Risk Assessment</h>
<h4 style='text-align:center;color:gray;'> Customer Risk Assessment using Machine Learning</h4>""",unsafe_allow_html=True)
st.sidebar.title("Loan Preduction")
st.sidebar.info(
    """
    Enter the Customer details.
    Click Predict to check weather the customer is likely to repay the loan.
    """
)
# Load the trained model
model = joblib.load("loan_model.pkl")

st.write("Enter customer details below:")
#input fields
col1,col2=st.columns(2)
with col1:
age = st.number_input("Age", min_value=18, max_value=100,value=25)

annual_income = st.number_input("Annual Income", min_value=0,value=50000)

current_balance = st.number_input("Current Balance", min_value=0,value=10000)

delinquency_history = st.number_input("Delinquency History", min_value=0,value=0)

education_level = st.selectbox(
    "Education Level",
    ["High School", "Bachelor", "Master", "PhD"]
)

employment_status = st.selectbox(
    "Employment Status",
    ["Employed", "Self-employed", "Unemployed"]
)

debt_to_income_ratio = st.number_input(
    "Debt to Income Ratio",
    min_value=0.0,
    max_value=100.0,
    value=20.0
)
with col2:
credit_score = st.number_input(
    "Credit Score",
    min_value=300,
    max_value=900,
    value=700
)
monthly_income = st.number_input(
    "Monthly Income",
    min_value=0,
    value=4000
)

interest_rate = st.number_input(
    "Interest Rate",
    min_value=0.0,
    value=5.0
)

installment = st.number_input(
    "Installment",
    min_value=0,
    value=500
)

grade_subgrade = st.number_input(
    "Grade Subgrade",
    min_value=0,
    value=1
)

total_credit_limit = st.number_input(
    "Total Credit Limit",
    min_value=0,
    value=50000
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0,
    value=10000
)
#Encoding
education_map={
    "High School":1,
    "Bachelor":0,
    "Master":2,
    "PhD":4,
    "other":3
  }
emp_map = {
        "Employed": 0,
        "Self-employed": 2,
        "Unemployed": 4,
        "student":3,
        "Retired":1
    }
#Preduction button
if st.button("Predict",use_container_width=True,type="primary"):
    # Convert employment status to the same numeric values used in training.
    # IMPORTANT: Change these mappings if your notebook used different encoding.
    input_data = pd.DataFrame({
    "age": [age],
    "monthly_income": [monthly_income],
    "interest_rate": [interest_rate],
    "installment": [installment],
    "annual_income": [annual_income],
    "grade_subgrade": [grade_subgrade],
    "total_credit_limit": [total_credit_limit],
    "current_balance": [current_balance],
    "delinquency_history": [delinquency_history],
    "education_level": [education_map[education_level]],
    "employment_status": [emp_map[employment_status]],
    "debt_to_income_ratio": [debt_to_income_ratio],
    "credit_score": [credit_score],
    "loan_amount": [loan_amount]
})
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success(" low risk- Loan likely to be repaid.")
    else:
        st.error("High Risk - Loan repayment risk detected.")
st.markdown("---")
st.markdown(
    "<center>Developed using python.Streamlit.Machine Learning</center>",unsafe_allow_html=True
)
