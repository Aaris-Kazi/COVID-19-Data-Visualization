from datetime import datetime
import pandas as pd
import numpy as np
data = pd.read_csv('covid_19_india.csv')
nlist = []
states = data['State']
# print(states)
nlist = list(dict.fromkeys(states))
# print(nlist)
# print('\n', states.unique())
x = data['Date'].min()
y = data['Date'].max()
print(x)
print(y)
x = datetime.strptime(x, '%Y-%m-%d')
y = datetime.strptime(y, '%Y-%m-%d')
delta = y - x
print(delta.days)