import pandas as pd
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
from data_preprocess import preprocess_data

def sanitize_filename(feature_name):
    return "".join([c if c.isalnum() else "_" for c in feature_name])

def visualize_data():
    data = preprocess_data()

    specific_features = ['Age', 'Number of sexual partners', 'First sexual intercourse', 'Num of pregnancies',
                         'Smokes (years)', 'Smokes (packs/year)', 'Hormonal Contraceptives (years)', 'IUD (years)',
                         'STDs (number)', 'Dx:Cancer', 'Biopsy']

    # Create correlation plot for specified features
    corr_data = data[specific_features].corr()
    print(corr_data)
    fig_1 = px.imshow(corr_data, labels=dict(color="Correlation"), x=corr_data.columns, y=corr_data.index, text_auto=True)
    fig_1.show()
    #fig_1.write_image('fig_1.jpg')

    # Create histograms for each specified feature
    for feature in specific_features:
        fig = px.histogram(data, x=feature)
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        fig.show()
        sanitized_feature = sanitize_filename(feature)
        #fig.write_image(f'fig_{sanitized_feature}.jpg')

    return data

visualize_data()
