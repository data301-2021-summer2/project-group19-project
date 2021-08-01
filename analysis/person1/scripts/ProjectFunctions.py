import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_profiling import ProfileReport




df = pd.read_csv("../../data/raw/meteors.csv")
df

def data(path):
    df2 = (
    df.rename(columns={"name":"Name given","nametype":"Classification of state","recclass": "Class","mass": "Mass", "fall": "Fall Type"})
    .dropna()
    .drop(['reclat', 'reclong'], axis=1)
      )
    return df2


def DataMass(path):
    df3= (
    df.rename(columns={"name":"Name given","nametype":"Classification of state","recclass": "Class","mass": "Mass", "fall": "Fall Type"})
    .sort_values('Mass', ascending = True)
    .drop(['reclat', 'reclong'], axis=1)
    .dropna()
        )
    return df3


def DataYear(path): 
    df4 = (
    df.rename(columns={"name":"Name given","nametype":"Classification of state","recclass": "Class","mass": "Mass", "fall": "Fall Type"})
    .sort_values("year", ascending=True)
    .drop(['reclat', 'reclong'], axis=1)
    .dropna()
)
    return df4

