# Customer Churn Prediction Analytics

## Project Overview
This project explores customer churn using Python and data analytics techniques. It investigates customer characteristics and behaviours that may be associated with customer attrition.

The objective is to identify patterns in customer churn, generate useful business insights, and eventually develop a machine learning model to predict customers who are likely to leave.

## Dataset
The project uses a synthetically generated dataset containing 5,000 customer records.

Key variables include:
- Customer ID
- Age
- Gender
- Tenure (months)
- Monthly Charges
- Total Charges
- Contract Type
- Internet Service
- Payment Method
- Support Calls
- Churn Status

**Note:** This is synthetic data generated using Python and NumPy. It does not represent actual customers.

## Tools and Technologies
- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SQL (planned)

## Data Generation
The dataset is generated using Python with NumPy random functions.

A fixed random seed (`42`) ensures reproducibility.

Churn probabilities are based on predefined assumptions involving:
- Contract type
- Customer tenure
- Number of customer support calls

## Exploratory Data Analysis

Initial analysis includes:

- Dataset inspection
- Missing-value checks
- Duplicate checks
- Descriptive statistics
- Customer distribution analysis
- Overall churn-rate calculation
- Churn analysis by contract type
- Churn analysis by payment method
- Churn analysis by internet service

### Preliminary Findings

The generated dataset currently shows:

- Total customers: 5,000
- Customers who churned: 1,174
- Customers retained: 3,826
- Overall churn rate: 23.48%

Month-to-month customers currently show a higher churn rate than customers on longer-term contracts.

Payment method and internet service show relatively small differences in churn rates in the current dataset.

These findings reflect the assumptions used to generate synthetic data and should not be interpreted as real-world causal relationships.

## Project Roadmap

- [x] Synthetic dataset generation
- [x] Initial data cleaning and validation
- [x] Exploratory data analysis
- [ ] Numerical variable analysis
- [ ] Data visualisation
- [ ] Feature engineering
- [ ] Machine learning model development
- [ ] Model evaluation
- [ ] Business recommendations

## Author

**Fidelis Mutsvauki**

Data Analyst | Actuarial Science Graduate
