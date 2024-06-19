import pandas as pd
from data_analysis import analyze_data

def preprocess_data():
    data, categorical_features, numerical_features = analyze_data()

    # Drop unnecessary rows 
    data.drop(['Smokes', 'Hormonal Contraceptives', 'IUD', 'STDs', 'STDs:cervical condylomatosis',
               'STDs: Number of diagnosis', 'STDs:AIDS','Dx:HPV', 'Dx:CIN', 'Dx', 'Hinselmann',
               'Schiller', 'Citology', 'STDs: Time since first diagnosis', 'STDs: Time since last diagnosis'],
              axis=1, inplace=True)

    # Remove rows with question marks
    data = data.replace('?', pd.NA).dropna()

    # Convert columns to appropriate data types
    data = data.apply(pd.to_numeric)

    # Identify categorical and numerical features
    categorical_features = data.select_dtypes("object").columns
    print(f"\nCategorical Features: {categorical_features}")
    numerical_features = data.select_dtypes("number").columns
    print(f"\nNumerical Features: {numerical_features}")

    print(data.head())
    
    return data

preprocess_data()
