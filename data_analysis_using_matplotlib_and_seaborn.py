# -*- coding: utf-8 -*-
"""data analysis using matplotlib and seaborn

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NJdSFX-KElutwsRiOKPVH3zbXthkV1e_

performing exploratory data analysis on diabetes dataset. Use the Matplotlib and Seaborn libraries for plotting.
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/content/diabetes.csv")

df.head(5)

df.tail(5)

df.dtypes

df = df.drop(['DiabetesPedigreeFunction'],axis=1)

df.head(5)

df = df.rename(columns={"BloodPressure": "BP", "SkinThickness": "SkinThick"})

df.head(5)

df.shape

df.size

duplicate_rows_df = df[df.duplicated()]
print("Shape of duplicate data: ", duplicate_rows_df.shape)

df.count()

df = df.drop_duplicates()
df.head(5)

df.count()

print(df.isnull().sum())

df = df.dropna()
df.count()

print(df.isnull().sum())

sns.boxplot(x=df['BP'])

sns.boxplot(x=df['BMI'])

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)

df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
df.shape

df.count()

df.Age.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
plt.title("Number persons age wise ")
plt.ylabel('Persons')
plt.xlabel('Age');

df.corr()

df['Outcome'].value_counts()

for col in df.columns:
    print("The minimum value for the columns {} is {}".format(col, df[col].min()))

for col in df.columns:
    print("The maximum value for the columns {} is {}".format(col, df[col].max()))

from scipy.stats import skew
for col in df.drop('Outcome', axis = 1).columns:
    print("Skewness for the column {} is {}".format(col, df[col].skew()))

