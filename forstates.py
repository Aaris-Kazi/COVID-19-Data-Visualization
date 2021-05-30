from datetime import date, datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def showdata():
    name = input('Enter the State Name:\t')
    data = pd.read_csv('covid_19_india.csv')
    try:
        city = data[data.State == name]
        if len(city) ==0:
            print('Enter the Right State Of India!')
        else:
            x= city['Date']
            y= city['Confirmed']
            z= city['Deaths']
            a= city['Cured']
            titles = 'Confirmed '+name+' COVID DATA '
            plt.title(titles)
            plt.xlabel('Dates')
            plt.ylabel('Number')
            plt.plot(x, y)
            plt.plot(x, z)
            plt.plot(x, a)
            plt.legend(['Confirmed', 'Deaths', 'Cured'])
            plt.grid(True)
            # plt.subplots_adjust(left = 0.05, right = 1.0)  
            plt.show()
    except Exception as e:
        print(e)