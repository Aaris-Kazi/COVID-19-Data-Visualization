from datetime import date, datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
def predicting():
    name = input('Enter the State Name:\t')
    data = pd.read_csv('covid_19_india.csv')
    try:
        city = data[data.State == name]
        if len(city) ==0:
            print('Enter the Right State Of India!')
        else:
            datelist = []
            x= city['Date']
            y= city['Confirmed']
            for i in x:
                j = datetime.strptime(i, '%Y-%m-%d')
                # print(j.date())
                datelist.append(j.date())
    
            reg = LinearRegression().fit([x], [y])
            exampledate = datetime.strptime("2020-05-20", '%Y-%m-%d')
                
            a = np.array([['2020-05-20']])
            b = reg.predict(a)
            print(b)
    except Exception as e:
        print(e)