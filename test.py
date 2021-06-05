from fordiff import difference
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
# from sklearn.datasets import make_classification
def predicting():
    # names = input('Enter the State Name:\t')
    names = 'Maharashtra'
    data = pd.read_csv('covid_19_india.csv')
    try:
        city = data[data.State == names]
        if len(city) ==0:
            print('Enter the Right State Of India!')
        else:
            dif, lx, ly =difference()
            days= []
            y= city['Confirmed']
            for i in range(0,len(y)):
                days.append(i)
            days = np.array(days)
            days = days.reshape(-1,1)
            conf = np.array(y)
            a = np.array([[437],[438],[439],[500],[550],[650], [800]])
            # clf = RandomForestClassifier(max_depth=2, random_state=0)
            # clas =clf.fit(X, y)
            # reg = LinearRegression().fit(days, conf)
            # b = reg.predict(a)
            x_train, x_test, y_train, x_test = train_test_split(days, conf, test_size= 0.30, random_state=42) 
            rreg = RandomForestRegressor()
            clas = rreg.fit(x_train, y_train)
            b = clas.predict(a)
            
            # b = clas.predict(a)
            print(b)
            plt.plot(days, conf)
            plt.scatter(a, b)
            lx = str(lx.date())
            ly = str(ly.date())
            # print(lx, ly)
            plt.title('Covid data between '+lx+' and '+ly)
            plt.legend(['Actual Number', 'Predicted Number'])
            plt.xlabel('Dates')
            plt.ylabel('Number of People')
            plt.grid(True)
            plt.savefig('plot.png', dpi=300, bbox_inches='tight')
            plt.show()
    except Exception as e:
        print(e)
predicting()