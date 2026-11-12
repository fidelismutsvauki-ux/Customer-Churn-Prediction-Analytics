import pandas as pd
import numpy as np
np.random.seed(42)
n=5000
##generate random data
data ={ 
  "customer_id":range (1001,1001+n),
  "age": np.random.randint(18,75,n),
  "gender": np.random.choice(["Male","Female"],n),
  "tenure_months": np.random.randint(1,73,n),
  "monthly_charges": np.random.uniform(20,150,n).round(2),
  "contract_type": :np.random.choice(["Month-to-month","One year","Two year"],n,
                                     p=[0.55,0.25,0.20]),
  "internet_service":np.random.choice(["DSL","Fibre optic","None"],n),
  "payment_method":np.random.choice(["Electronic","Credit card","Bank transfer"],n),
  "support_calls":np.random.poisson(2,n),
  "total_charges":np.zeros(n)

##calculate total charges
  df= pd.DataFrame(data)
df["total_charges"]= df["monthly_charges"]*df["tenure_months"]).round(2)

##generate customer churn probability
churn_score = (0.15+0.12*(df["contract_type"]=="Month-to-month")+0.08*df["tenure_months"]<12)+0.08*(df["support_calls"]>3))
churn_probability = 
