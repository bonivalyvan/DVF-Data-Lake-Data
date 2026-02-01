import os
import pandas as pd 
print ("\taggregated")
df_aggregated = pd.read_csv('../data_lake/raw/dvf_statistics_aggregated.csv') 
print(df_aggregated.info()) 
print(df_aggregated.head())
print('Rows:', len(df_aggregated)) 
print(df_aggregated.isna().sum())

print ("\tmonthly")
df_monthly = pd.read_csv('../data_lake/raw/dvf_statistics_monthly.csv')
print(df_monthly.info())
print(df_monthly.head())
print('Rows:', len(df_monthly)) 
print(df_monthly.isna().sum())