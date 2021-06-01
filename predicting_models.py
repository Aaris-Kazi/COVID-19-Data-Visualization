from datetime import date, datetime
from fordiff import difference
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
def predicting():
    # names = input('Enter the State Name:\t')
    names = 'Kerala'
    data = pd.read_csv('covid_19_india.csv')
    try:
        city = data[data.State == names]
        if len(city) ==0:
            print('Enter the Right State Of India!')
        else:
            dif, x, y =difference()
            days= []
            confirms = []
            # print(dif, x, y)
            y= city['Confirmed']
            for i in range(0,len(y)):
                days.append(i)
            # x= city['Date']
            print(days)
            days = np.array(days)
            # print(days.reshape(-1,1))
            # print(y)
            # print(confirms)
            # reg = LinearRegression().fit([days], [y])
            # a = np.array([[476]])
            # b = reg.predict(a)
            # print(b)
    except Exception as e:
        print(e)