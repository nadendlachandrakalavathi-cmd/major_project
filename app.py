import streamlit as st
import joblib
import pandas as pd
st.set_page_config(
    page_title="Bank Loan Repayment Analysis and Customer Risk Assessment",
    page_icon="🏦",
    layout="wide"
)
st.markdown("""
<h1 style='text-align:center;color:#1E88E5;'>🏦Bank Loan Repayment Analysis and Customer Risk Assessment</h>
<h4 style='text-align:center;color:gray;'> Customer Risk Assessment using Machine Learning</h4>""",unsafe_allow_html=True)
st.sidebar.title("🗒️Loan Preduction")
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
col1,col2,col3=st.columns(3)
with col1:
    age = st.number_input("Age", min_value=18, max_value=100,value=25)
    gender=st.selectbox(
        ["Male",
    "Female",
    "Other"]
    )
    marital_ststus=st.selectbox(
        ["Single",
        "Married",
        "Divorced",
        "Widowed"]
    )
    education_level=st.selectbox(
        ["Education Level",
        "High School",
        "Bachelor's",
        "Master's",
        "PhD",
        "Other"]
    )   
    employment_status = st.selectbox(
        ["Employed",
        "Self-employed",
        "Student",
        "Unemployed",
        "Retired"]
    )
    monthly_income = st.number_input(
        "Monthly Income",
        min_value=0,
        value=4000
    )
with col2:    
    annual_income = st.number_input("Annual Income", min_value=0,value=50000)

    current_balance = st.number_input("Current Balance", min_value=0,value=10000)

    delinquency_history = st.number_input("Delinquency History", min_value=0,value=0)

    debt_to_income_ratio = st.number_input(
        "Debt to Income Ratio",
        min_value=0.0,
        max_value=100.0,
        value=20.0
    )
    interest_rate = st.number_input(
        "Interest Rate",
        min_value=0.0,
        value=5.0
    )
    total_credit_limit = st.number_input(
        "Total Credit Limit",
        min_value=0,
        value=50000
    )
with col3:
    credit_score = st.number_input(
        "Credit Score",
        min_value=300,
        max_value=900,
        value=700
    )
    installment = st.number_input(
        "Installment",
        min_value=0,
        value=500
    )
    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0,
        value=10000
    )
    
    loan_purpose= st.selectbox(
        ["Car",
        "Debt consolidation",
        "Business",
        "Home",
        "Medical",
        "Education",
        "Vacation",
        "Other"]
    )
    
    grade_subgrade =st.selectbox(
        ["A1", "A2", "A3", "A4", "A5",
        "B1", "B2", "B3", "B4", "B5",
        "C1", "C2", "C3", "C4", "C5",
        "D1", "D2", "D3", "D4", "D5",
        "E1", "E2", "E3", "E4", "E5",
        "F1", "F2", "F3", "F4", "F5"]
    )

#Preduction button
if st.button("🔍Predict",use_container_width=True,type="primary"):
    # Convert employment status to the same numeric values used in training.
    # IMPORTANT: Change these mappings if your notebook used different encoding.
    gender_map = {
        "Male": 0,
        "Female": 1,
        "Other": 2
    }

    marital_map = {
        "Single": 0,
        "Married": 1,
        "Divorced": 2,
        "Widowed": 3
    }

    education_map = {
        "High School": 0,
        "Bachelor's": 1,
        "Master's": 2,
        "PhD": 3,
        "Other": 4
    }

    employment_map = {
        "Employed": 0,
        "Self-employed": 1,
        "Student": 2,
        "Unemployed": 3,
        "Retired": 4
    }

    loan_purpose_map = {
        "Car": 0,
        "Debt consolidation": 1,
        "Business": 2,
        "Home": 3,
        "Medical": 4,
        "Education": 5,
        "Vacation": 6,
        "Other": 7
    }

    grade_map = {
        "A1":0, "A2":1, "A3":2, "A4":3, "A5":4,
        "B1":5, "B2":6, "B3":7, "B4":8, "B5":9,
        "C1":10, "C2":11, "C3":12, "C4":13, "C5":14,
        "D1":15, "D2":16, "D3":17, "D4":18, "D5":19,
        "E1":20, "E2":21, "E3":22, "E4":23, "E5":24,
        "F1":25, "F2":26, "F3":27, "F4":28, "F5":29
    }

input_data = pd.DataFrame({
    "age": [age],
    "gender":[gender],
    "marital_status":[marital_ststus],
    "education_level":[education_level],
    "employment_status":[employment_status],
    "monthly_income": [monthly_income],
    "annual_income": [annual_income],
    "current_balance": [current_balance],
    "delinquency_history": [delinquency_history],
    "debt_to_income_ratio": [debt_to_income_ratio],
    "interest_rate": [interest_rate],
    "total_credit_limit": [total_credit_limit],
    "credit_score": [credit_score],
    "installment": [installment],
    "loan_amount": [loan_amount],
    "loan_purpose":[loan_purpose],
    "grade_subgrade":[grade_subgrade]
})
prediction = model.predict(input_data)

if prediction[0] == 1:
        st.success(" ✅- Loan likely to be repaid.")
else:
        st.error(" ❌- Loan repayment risk detected.")
st.markdown("---")
st.markdown(
    "<center>Developed using python.Streamlit.Machine Learning</center>",unsafe_allow_html=True
)
