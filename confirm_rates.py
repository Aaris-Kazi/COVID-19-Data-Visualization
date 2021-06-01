import pandas as pd

names = 'Goa'
data = pd.read_csv('covid_19_india.csv')
city = data[data.State == names]
y= city['Confirmed']
# print(y)
n = len(y)
print(n)
# for i in range(n):
#     x = y[i]
print(y[371])