import pandas as pd
import numpy as np
data = pd.read_csv('covid_19_india.csv')
nlist = []
states = data['State']
# print(states)
nlist = list(dict.fromkeys(states))
print(len(nlist))
        