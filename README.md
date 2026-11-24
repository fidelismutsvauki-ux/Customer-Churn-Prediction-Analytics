# Customer Churn Prediction Analytics

**Author:** Fidelis Mutsvauki  
**Role:** Data Analyst | Actuarial Science Graduate  
**Tools:** Python | Jupyter Notebook | Pandas | NumPy | Matplotlib | Seaborn

---

## 1. Project Overview

This project focuses on analysing customer churn using Python and data analytics techniques.

Customer churn occurs when customers stop using a company's products or services. Understanding the factors associated with customer churn helps businesses identify potential customer losses and develop strategies to improve customer retention.

The main objectives of this project are to:

- Explore customer behaviour and characteristics.
- Identify patterns associated with customer churn.
- Calculate and analyse customer churn rates.
- Visualise important customer trends.
- Develop a machine learning model to predict potential customer churn.
- Generate actionable business recommendations.

## 2. Dataset Description

The project uses a synthetically generated dataset containing **5,000 customer records**.

The dataset includes the following variables:

| Variable | Description |
|---|---|
| customer_id | Unique customer identifier |
| age | Customer's age |
| gender | Customer's gender |
| tenure_months | Number of months the customer has stayed |
| monthly_charges | Monthly amount charged |
| total_charges | Total amount charged over the customer's tenure |
| contract_type | Customer's contract arrangement |
| internet_service | Type of internet service |
| payment_method | Customer's payment method |
| support_calls | Number of customer support calls |
| churn | Whether the customer left (1) or stayed (0) |

**Important:** This is synthetic data generated using Python and NumPy. It does not represent actual customer records.

## 3. Tools and Technologies

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SQL (planned)

## 4. Data Generation

The dataset was generated using Python and NumPy random functions.

A fixed random seed (`42`) was used to ensure reproducibility.

Customer churn probabilities were determined using predefined assumptions involving:

- Contract type.
- Customer tenure.
- Number of customer support calls.

The generated churn outcome is a binary variable:

- `1` = Customer churned.
- `0` = Customer retained.

## 5. Data Cleaning and Validation

Initial data validation included:

- Checking dataset dimensions.
- Inspecting data types.
- Identifying missing values.
- Checking duplicate records.
- Reviewing categorical variables.
- Generating descriptive statistics.

The dataset currently contains 5,000 records with no missing values or duplicate rows.

## 6. Exploratory Data Analysis (EDA)

Exploratory analysis examines customer characteristics and their relationship with churn.

The analysis includes:

- Overall customer churn rate.
- Churn distribution.
- Churn by contract type.
- Churn by payment method.
- Churn by internet service.
- Customer summary statistics.

### 6.1 Overall Churn Results

| Metric | Result |
|---|---:|
| Total Customers | 5,000 |
| Customers Churned | 1,174 |
| Customers Retained | 3,826 |
| Overall Churn Rate | 23.48% |

### 6.2 Churn by Contract Type

| Contract Type | Churn Rate |
|---|---:|
| Month-to-month | 27.71% |
| One year | 18.60% |
| Two year | 18.35% |

Month-to-month customers currently exhibit a higher churn rate than customers on longer-term contracts.
![Churn by Contract Type](images/churn_contract.png)

### 6.3 Churn by Payment Method

The analysis compares churn rates among customers using:

- Bank transfer.
- Credit card.
- Electronic payment.

The observed differences are relatively small.

### 6.4 Churn by Internet Service

The analysis compares churn rates among customers using:

- DSL.
- Fibre optic.
- No service.

The observed differences are relatively small.

**Interpretation:** These findings reflect the assumptions used to generate synthetic data. They should not be interpreted as proof of real-world customer behaviour or causal relationships.

## 7. Predictive Modelling

After completing Exploratory Data Analysis (EDA), predictive modelling was introduced using Python's Scikit-learn library.

### 7.1 Data Preparation

The dataset was prepared for machine learning by:

- Encoding categorical variables using `pd.get_dummies()`.
- Splitting the dataset into training and testing sets using `train_test_split()`.

The resulting dataset dimensions were:

| Dataset | Shape |
|---|---|
| Training Features (X_train) | (4000, 12) |
| Testing Features (X_test) | (1000, 12) |
| Training Target (y_train) | (4000,) |
| Testing Target (y_test) | (1000,) |

### 7.2 Logistic Regression

The first machine learning algorithm implemented was Logistic Regression.

The initial model achieved **76.5% accuracy**. However, despite this accuracy, it failed to identify customers who actually churned.

This highlighted the impact of class imbalance on model performance.

### 7.3 Addressing Class Imbalance

To improve the model's ability to identify customers likely to churn, Logistic Regression was retrained using:

`class_weight='balanced'`

This adjustment gave greater importance to the minority class (customers who churned).

The balanced model achieved the following results:

| Metric | Result |
|---|---:|
| Accuracy | 54.8% |
| Churn Precision | 28% |
| Churn Recall | 61% |
| Churn F1-score | 39% |

The balanced model improved churn recall from **0% to 61%**, allowing it to identify a significantly larger proportion of customers who churned.

### 7.4 Confusion Matrix

The balanced Logistic Regression model produced the following confusion matrix:

```text
[[405 360]
 [ 92 143]]
```

### 7.5 Random Forest Classifier

A Random Forest Classifier was introduced as an alternative to Logistic Regression to improve churn prediction performance.

The model combines multiple decision trees to produce predictions and capture complex relationships within the dataset.

### 7.6 Feature Importance Analysis

Feature importance was extracted from the Random Forest model to identify the most influential predictors of customer churn.

The leading features included:

| Feature | Importance |
|---|---:|
| Total Charges | 0.2025 |
| Monthly Charges | 0.1714 |
| Tenure Months | 0.1598 |
| Age | 0.1282 |
| Contract Type (One Year) | 0.0979 |
| Support Calls | 0.0851 |

Total charges, monthly charges and customer tenure emerged as the most influential features.

### 7.7 Hyperparameter Tuning

GridSearchCV was used to optimise the Random Forest model by testing different combinations of hyperparameters through 5-fold cross-validation.

The parameters tested included:

- `n_estimators`: 100, 200, 300
- `max_depth`: 5, 10, 20, None
- `min_samples_split`: 2, 5, 10
- `min_samples_leaf`: 1, 2, 4

Recall was selected as the scoring metric to improve the identification of customers likely to churn.

### 7.8 Model Evaluation

The tuned Random Forest model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

The model achieved:

- Accuracy: 54.7%
- Recall: 64%

### 7.9 Confusion Matrix Analysis

A confusion matrix was generated to assess the classification performance of the tuned Random Forest model.

The visualisation identifies:

- Correctly predicted customers who stayed.
- Correctly predicted customers who churned.
- Customers incorrectly classified as staying.
- Customers incorrectly classified as churning.

### 7.10 Model Visualisation

Visualisations were generated to communicate the model's performance and findings.

These included:

- Confusion Matrix Heatmap.
- Random Forest Feature Importance Chart.

The visualisations provide a clearer understanding of the model's predictive performance and the variables influencing customer churn.

## 8. Expected Business Value

The completed project aims to demonstrate how data analytics and predictive modelling can help businesses:

- Identify customers who may be at risk of leaving.
- Understand customer retention patterns.
- Improve customer relationship management.
- Support data-driven retention strategies.
- Make better business decisions using customer data.

## 9. Project Structure

The repository is organised into folders for data, notebooks, source code, and visualisations.

These folders will contain the relevant project files as development progresses.

---

**Fidelis Mutsvauki**  
*Data Analyst | BSc Honours Actuarial Science*
