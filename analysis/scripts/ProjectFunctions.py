import pandas as pd


def data(path):
#cleaned and dropped overall data  
    dc = (
    df.rename(columns={"name":"Name given","nametype":"Classification of state","recclass": "Class","mass": "Mass", "fall": "Fall Type"})
    .sort_values("year", ascending=True)
    .dropna()
    .drop(['reclat', 'reclong'], axis=1)
         )
    return dc


def DataMass(path):
#method chain starts  - defines mass using cleaned data
    df1 = (
        pd.read_csv(path)
          )
    
    df2= (
        dc.sort_values(['Mass'], ascending = (True))
        )
        
    return df2


def DataYear(path):
 #method chain starts - defines year using cleaned data
    df3 = (
        pd.read_csv(path)
          )
    
    df4 = (
        dc.sort_values(['year'], ascending = (True))
          )
    return df4