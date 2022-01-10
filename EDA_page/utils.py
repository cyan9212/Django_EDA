import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO
import numpy as np
import pandas as pd


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y):
    heart_df = pd.read_csv("/srv/Django_EDA/EDA_page/heart.csv")
    drop_index = heart_df[heart_df['RestingBP'] == 0].index.values[0]
    heart_df.drop(index=drop_index, axis=0, inplace=True)
    numeric = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']
    plt.switch_backend('AGG')
    sns.set_palette(sns.hls_palette(10, h=0.5))
    plt.figure(figsize=(8, 5))
    plt.title(x+' & '+y, size=15, fontweight='bold', y=1.1)
    if x in numeric and y in numeric:
        sns.scatterplot(x, y, data=heart_df)
    elif x in numeric and y not in numeric:
        sns.barplot(x, y, data=heart_df)
    elif x not in numeric and y in numeric:
        sns.barplot(y, x, data=heart_df)
    else:
        sns.catplot(x, y, data=heart_df)
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_plot_hue(x, y, hue):
    heart_df = pd.read_csv("/srv/Django_EDA/EDA_page/heart.csv")
    drop_index = heart_df[heart_df['RestingBP'] == 0].index.values[0]
    heart_df.drop(index=drop_index, axis=0, inplace=True)
    numeric = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']
    plt.switch_backend('AGG')
    sns.set_palette(sns.hls_palette(10, h=0.5))
    plt.figure(figsize=(8, 5))
    plt.title(x+' & '+y , size=15, fontweight='bold', y=1.1)
    if x in numeric and y in numeric:
        sns.scatterplot(x, y, hue=hue, data=heart_df)
    elif x in numeric and y not in numeric:
        sns.barplot(y, x, hue=hue, data=heart_df)
    elif x not in numeric and y in numeric:
        sns.barplot(x, y, hue=hue, data=heart_df)
    else:
        sns.catplot(x, y, hue=hue, data=heart_df)
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_hist(x):
    heart_df = pd.read_csv("/srv/Django_EDA/EDA_page/heart.csv")
    drop_index = heart_df[heart_df['RestingBP'] == 0].index.values[0]
    heart_df.drop(index=drop_index, axis=0, inplace=True)
    numeric = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']
    plt.switch_backend('AGG')
    sns.set_palette(sns.hls_palette(10, h=0.5))
    plt.figure(figsize=(8, 5))
    plt.title(x, size=15, fontweight='bold', y=1.1)
    if x in numeric:
        sns.kdeplot(x, fill=True, data=heart_df)
    else:
        sns.countplot(x, data=heart_df)
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_hist_hue(x, hue):
    heart_df = pd.read_csv("/srv/Django_EDA/EDA_page/heart.csv")
    drop_index = heart_df[heart_df['RestingBP'] == 0].index.values[0]
    heart_df.drop(index=drop_index, axis=0, inplace=True)
    numeric = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']
    plt.switch_backend('AGG')
    sns.set_palette(sns.hls_palette(10, h=0.5))
    plt.figure(figsize=(8, 5))
    plt.title(x, size=15, fontweight='bold', y=1.1)
    if x in numeric:
        sns.kdeplot(x, hue=hue, fill=True, data=heart_df)
    else:
        sns.countplot(x, hue=hue, data=heart_df)
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_empty_plot():
    plt.switch_backend('AGG')
    sns.set_palette(sns.hls_palette(10, h=0.5))
    plt.figure(figsize=(8, 5))
    plt.plot()
    plt.tight_layout()
    graph = get_graph()
    return graph