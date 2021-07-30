import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_profiling import ProfileReport




def data(path):
#cleaned and dropped overall data  
    df2 = (
    df.rename(columns={"name":"Name given","nametype":"Classification of state","recclass": "Class","mass": "Mass", "fall": "Fall Type"})
    .sort_values("year", ascending=True)
    .dropna()
    .drop(['reclat', 'reclong'], axis=1)
         )
    return df2


def DataMass(path):
#method chain starts  - defines mass using cleaned data
   df3 = (
        pd.read_csv(path)
          )
    
    df4= (
        df2.sort_values(['Mass'], ascending = (True))
        )
    return df4


def DataYear(path):
 #method chain starts - defines year using cleaned data
    df5 = (
        pd.read_csv(path)
          )
    
    df6 = (
        df2.sort_values(['year'], ascending = (True))
          )
    return df6
