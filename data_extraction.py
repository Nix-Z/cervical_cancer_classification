import pandas as pd

def load_data():
  data = pd.read_csv('risk_factors_cervical_cancer.csv')
  print(data.head())
  return data

load_data()
