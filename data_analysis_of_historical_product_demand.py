# -*- coding: utf-8 -*-
"""Data Analysis of Historical product demand.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KBsI8eDJU3VkHD2R2a6jqOYuYovzNPhh

# Data View

# Importing the data for analysis
"""

'''Importing data'''
import pandas as pd
df = pd.read_csv('/content/Historical Product Demand.csv')
df

from matplotlib import pyplot as plt
df['Order_Demand'].plot(kind='hist', bins=20, title='Order_Demand')
plt.gca().spines[['top', 'right',]].set_visible(False)

from matplotlib import pyplot as plt
import seaborn as sns
df.groupby('Warehouse').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

df.info()

"""# Generate a summary of the dataset"""

df.describe()

"""# Review the first few rows of the dataset"""

'''getting first 5 rows'''
df.head()

"""# Review the last few rows of the dataset"""

'''getting last 5 rows'''
df.tail()

"""# Cleaning of the data for the analysis"""

'''Drop any missing values'''
df.dropna()

'''Convert Dates to datetime'''
df['Date'] = pd.to_datetime(df['Date'])
df

'''remove the negative order demand'''
df1=df[df['Order_Demand']>0]
df1

'''remove the duplicates'''
df2=df1.drop_duplicates()
df2

"""# Calculate descriptive statistics for Order_Demand"""

'''Analayis Daily total demand'''
df3=df2.groupby('Date')['Order_Demand'].sum()
df3

'''Basic descriptive statistics for Order_Demand'''
df3.describe()

'''Count of unique products, categories, and warehouses'''
df4=df2.nunique()
df4

'''Demand by Warehouse'''
df5=df2.groupby('Warehouse')['Order_Demand'].sum()
df5

'''Demand by product category'''
df6=df2.groupby('Product_Category')['Order_Demand'].sum()
df6

'''Demand by product Code'''
df7=df2.groupby('Product_Code')['Order_Demand'].sum()
df7

"""# First top 10 product by order demand"""

'''Top 10 product by order demand'''
df8=df2.groupby('Product_Code')['Order_Demand'].sum().sort_values(ascending=False).head(10)
df8

'''plot a graph for the df8'''
df8.plot(kind='bar')

'''Arrange the data by order of demand'''
df9=df2.sort_values('Order_Demand', ascending=False)
df9

from matplotlib import pyplot as plt
import seaborn as sns
def _plot_series(series, series_name, series_index=0):
  palette = list(sns.palettes.mpl_palette('Dark2'))
  xs = series['Date']
  ys = series['Order_Demand']

  plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)])

fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')
df_sorted = df9.sort_values('Date', ascending=True)
for i, (series_name, series) in enumerate(df_sorted.groupby('Warehouse')):
  _plot_series(series, series_name, i)
  fig.legend(title='Warehouse', bbox_to_anchor=(1, 1), loc='upper left')
sns.despine(fig=fig, ax=ax)
plt.xlabel('Date')
_ = plt.ylabel('Order_Demand')

from matplotlib import pyplot as plt
import seaborn as sns
df9.groupby('Warehouse').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

from matplotlib import pyplot as plt
import seaborn as sns
figsize = (12, 1.2 * len(df9['Warehouse'].unique()))
plt.figure(figsize=figsize)
sns.violinplot(df9, x='Order_Demand', y='Warehouse', inner='box', palette='Dark2')
sns.despine(top=True, right=True, bottom=True, left=True)

from matplotlib import pyplot as plt
df9['Order_Demand'].plot(kind='hist', bins=20, title='Order_Demand')
plt.gca().spines[['top', 'right',]].set_visible(False)

"""# Analysis of a range of times of high order demand with product code"""

''' finding range of date of high order demand with product code'''
df10=df2.groupby(['Product_Code','Date'])['Order_Demand'].sum().sort_values(ascending=False).head(10)
df10

'''plot a graph for the df10'''
df10.plot(kind='bar')

'''finding range of date of high order demand with top product code and top product category'''
df11=df2.groupby(['Product_Code','Product_Category','Date'])['Order_Demand'].sum().sort_values(ascending=False).head(10)
df11

'''plot a graph for the df11'''
df11.plot(kind='bar')

'''Daily Demand Trends'''
df12=df2.groupby('Date')['Order_Demand'].sum()
df12

"""# Top Product Catagory Analysis"""

'''Top Product Catagory Analysis'''
df13=df2.groupby('Product_Category')['Order_Demand'].sum().sort_values(ascending=False).head(10)
df13

