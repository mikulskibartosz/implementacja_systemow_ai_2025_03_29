import os
import pandas as pd
from sklearn.model_selection import train_test_split


data = pd.read_csv("https://raw.githubusercontent.com/sharmaroshan/Churn-Modelling-Dataset/refs/heads/master/Churn_Modelling.csv")

x = data.copy().drop(columns=['CustomerId', 'Surname', 'RowNumber', 'Exited'])
y = data['Exited']

x = pd.get_dummies(x)

print("x.shape", x.shape)
print("y.shape", y.shape)

print("x.columns", x.columns)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 42)

print("x_train.shape", x_train.shape)
print("y_train.shape", y_train.shape)
print("x_test.shape", x_test.shape)
print("y_test.shape", y_test.shape)

if not os.path.exists('data'):
    os.makedirs('data')

x_train.to_csv('data/x_train.csv', index=False)
y_train.to_csv('data/y_train.csv', index=False)
x_test.to_csv('data/x_test.csv', index=False)
y_test.to_csv('data/y_test.csv', index=False)

print("Data saved to data/ directory")
