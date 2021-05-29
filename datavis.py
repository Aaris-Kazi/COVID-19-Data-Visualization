from datetime import date, datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

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
            plt.title('Confirmed COVID DATA')
            plt.xlabel('Dates')
            plt.ylabel('Number')
            plt.legend(['Confirmed', 'Deaths', 'Cured'])
            plt.plot(x, y)
            plt.plot(x, z)
            plt.plot(x, a)
            plt.grid(True)
            # plt.subplots_adjust(left = 0.05, right = 1.0)  
            plt.show()
    except Exception as e:
        print(e)
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

def main():
    showdata()
    # predicting()
if __name__ == '__main__':
    main()

