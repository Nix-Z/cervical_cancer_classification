import pandas as pd
import numpy as np
from sklearn.utils import resample
from datavisualization import visualize_data

def engineer_features():
    data = visualize_data()

    # Balance data --> Biopsy
    data_majority = data[data['Biopsy']==0]
    data_minority = data[data['Biopsy']==1]
    data_minority_upsampled = resample(data_minority, replace=True, n_samples=623, random_state=1)
    data_upsampled = pd.concat([data_majority, data_minority_upsampled], axis=0)

    print(data_upsampled['Biopsy'].groupby(data_upsampled['Biopsy']).count())
    print(data_upsampled.head())

    data_upsampled.to_csv('cervical_cancer_cleansed_data.csv', index=False)
    
    return data_upsampled

engineer_features()
