from datetime import datetime
import pandas as pd
def difference():
    data = pd.read_csv('covid_19_india.csv')
    x = data['Date'].min()
    y = data['Date'].max()
    print(x)
    print(y)
    x = datetime.strptime(x, '%Y-%m-%d')
    y = datetime.strptime(y, '%Y-%m-%d')
    delta = y - x
    print(delta.days)
    return int(delta.days), x, y