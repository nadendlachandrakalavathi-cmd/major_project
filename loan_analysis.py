import mysql.connector
import pandas as pd
#database connection
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "chandrakala@2004",
    database="bank_loan_analysis"
)
cursor = conn.cursor()
queries =[
    
    # number of records
            "select count(*)as total_records from cleaned_loan_dataset ",

    # total_customers
            "select count(*) as total_customers from cleaned_loan_dataset",

    # avg_annual_income
            "select avg(annual_income) as avg_income from cleaned_loan_dataset",

    # Loan Repayment Rate
            """SELECT
            loan_paid_back,
            COUNT(*) AS customers,
            ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM cleaned_loan_dataset ), 2) AS percentage
            FROM cleaned_loan_dataset 
            GROUP BY loan_paid_back""",

    # Average Financial Profile of Customers
            """SELECT
            ROUND(AVG(annual_income),2) AS avg_annual_income,
            ROUND(AVG(credit_score),2) AS avg_credit_score,
            ROUND(AVG(loan_amount),2) AS avg_loan_amount
            FROM cleaned_loan_dataset""",

    # Gender-Wise Repayment Analysis
            """SELECT
            gender,
            loan_paid_back,
            COUNT(*) AS customers
            FROM cleaned_loan_dataset
            GROUP BY gender, loan_paid_back
            ORDER BY gender""",

    # Education Level VS Loan Repayment
            """SELECT
            education_level,
            loan_paid_back,
            COUNT(*) AS customers
            FROM cleaned_loan_dataset
            GROUP BY education_level, loan_paid_back
            ORDER BY education_level""",

    # Employment Status Risk Analysis
            """SELECT
            employment_status,
            COUNT(*) AS total_customers,
            ROUND(AVG(credit_score),2) AS avg_credit_score
            FROM cleaned_loan_dataset
            GROUP BY employment_status""",

    # Loan Purpose Analysis
            """SELECT
            loan_purpose,
            COUNT(*) AS total_loans,
            ROUND(AVG(loan_amount),2) AS avg_loan_amount
            FROM cleaned_loan_dataset
            GROUP BY loan_purpose
            ORDER BY total_loans DESC""",

    # Credit Score Category Analysis
            """SELECT
            CASE
            WHEN credit_score >= 750 THEN 'Excellent'
            WHEN credit_score >= 700 THEN 'Good'
            WHEN credit_score >= 650 THEN 'Fair'
            ELSE 'Poor'
            END AS credit_category,
            COUNT(*) AS customers
            FROM cleaned_loan_dataset
            GROUP BY credit_category""",

    # High Risk Customers
            """SELECT
            age,
            annual_income,
            credit_score,
            debt_to_income_ratio,
            loan_amount
            FROM cleaned_loan_dataset
            WHERE credit_score < 600
            AND debt_to_income_ratio > 40""",

    # Top 10 Customers by Loan Amount
            """SELECT
            age,
            annual_income,
            credit_score,
            loan_amount
            FROM cleaned_loan_dataset
            ORDER BY loan_amount DESC
            LIMIT 10""",

    # Repayment Performance by Credit Score
            """SELECT
            loan_paid_back,
            ROUND(AVG(credit_score),2) AS avg_credit_score
            FROM cleaned_loan_dataset
            GROUP BY loan_paid_back""",
    # Debt-to-income Ratio impact
            """SELECT
            loan_paid_back,
            ROUND(AVG(debt_to_income_ratio),2) AS avg_dti_ratio
            FROM cleaned_loan_dataset
            GROUP BY loan_paid_back""",
    # Delinquency Analysis
        """SELECT
            delinquency_history,
            COUNT(*) AS customers
            FROM cleaned_loan_dataset
            GROUP BY delinquency_history
            ORDER BY customers DESC""",
    # Public Record Analysis
        """SELECT
        public_records,
        COUNT(*) AS customers
        FROM cleaned_loan_dataset
        GROUP BY public_records
        ORDER BY public_records""",
    # Customer Risk Segmentation
        """SELECT
        CASE
        WHEN credit_score >= 750 THEN 'Low Risk'
        WHEN credit_score >= 650 THEN 'Medium Risk'
        ELSE 'High Risk'
        END AS risk_category,
        COUNT(*) AS customers
        FROM cleaned_loan_dataset
        GROUP BY risk_category"""
]
for query in queries:
    print("Query:",query)
    print("output:")
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
cursor.close()
conn.close()