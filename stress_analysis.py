#import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#load dataset
dataframe = pd.read_csv('data/StressLevelDataset.csv')

#basic info
print("First 5 rows")
print(dataframe.head())
print("\nDataset info:")
print(dataframe.info())
print("\nSummary statistics:")
print(dataframe.describe())
print("\nMissing values:")
print(dataframe.isnull().sum())

#correlation heatmap
plt.figure(figsize=(12,8))
sns.heatmap(dataframe.corr(), cmap="coolwarm")
plt.title("correlation matrix")
plt.savefig("heatmap.png")
plt.show()

#visualize stress level distibution
sns.countplot(x='stress_level', data=dataframe)
plt.title("stress level distribution")
plt.savefig("distribution.png")
plt.show()

#features (x) and target (y)
X = dataframe.drop('stress_level', axis=1) #remove columns
y = dataframe['stress_level']

#split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

#predictions
y_pred = model.predict(X_test)

#accurracy
accuracy = accuracy_score(y_test, y_pred)
print("\nModel accuracy:")
print(accuracy)
















