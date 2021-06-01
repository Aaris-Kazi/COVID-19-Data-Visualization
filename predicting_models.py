from datetime import date, datetime
from os import truncate
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
            y= city['Confirmed']
            for i in range(0,len(y)):
                days.append(i)
            
            days = np.array(days)
            days = days.reshape(-1,1)
            conf = np.array(y)
            # print(days)
            # print(conf)
            conf = conf.reshape(-1,1)
            reg = LinearRegression().fit(days, conf)
            a = np.array([[476]])
            b = reg.predict(a)
            print(b)
            plt.plot(days,conf)
            plt.scatter(a, b)
            plt.grid(True)
            plt.show()
    except Exception as e:
        print(e)