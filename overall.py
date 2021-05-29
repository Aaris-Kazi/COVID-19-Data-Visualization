from datetime import date, datetime
import matplotlib.pyplot as plt
import pandas as pd

def alldata():
    data = pd.read_csv('covid_19_india.csv')
    states = data['State']
    nlist = list(dict.fromkeys(states))
    try:
        kl = data[data.State == nlist[0]]
        tl = data[data.State == nlist[1]]
        dl = data[data.State == nlist[2]]
        rj = data[data.State == nlist[3]]
        up = data[data.State == nlist[4]]
        hy = data[data.State == nlist[5]]
        ld = data[data.State == nlist[6]]
        tn = data[data.State == nlist[7]]
        kt = data[data.State == nlist[8]]
        mh = data[data.State == nlist[9]]
        pb = data[data.State == nlist[10]]
        jk = data[data.State == nlist[11]]
        ap = data[data.State == nlist[12]]
        uk = data[data.State == nlist[13]]
        od = data[data.State == nlist[14]]
        py = data[data.State == nlist[15]]
        wb = data[data.State == nlist[16]]
        ch = data[data.State == nlist[17]]
        cg = data[data.State == nlist[18]]
        gj = data[data.State == nlist[19]]
        hp = data[data.State == nlist[20]]
        mp = data[data.State == nlist[21]]
        br = data[data.State == nlist[22]]
        mn = data[data.State == nlist[23]]
        mz = data[data.State == nlist[24]]
        nc = data[data.State == nlist[25]]
        ga = data[data.State == nlist[26]]
        am = data[data.State == nlist[28]]
        
        plt.title('Confirmed COVID DATA')
        plt.xlabel('Dates')
        plt.ylabel('Number')
        plt.plot(kl['Date'], kl['Confirmed'])
        plt.plot(tl['Date'], tl['Confirmed'])
        plt.plot(dl['Date'], dl['Confirmed'])
        plt.plot(rj['Date'], dl['Confirmed'])
        plt.plot(up['Date'], dl['Confirmed'])
        plt.plot(hy['Date'], dl['Confirmed'])
        plt.plot(dl['Date'], dl['Confirmed'])
        plt.plot(dl['Date'], dl['Confirmed'])
        plt.plot(dl['Date'], dl['Confirmed'])
        plt.plot(dl['Date'], dl['Confirmed'])
        plt.plot(dl['Date'], dl['Confirmed'])
        plt.plot(dl['Date'], dl['Confirmed'])
        plt.plot(dl['Date'], dl['Confirmed'])
        plt.plot(dl['Date'], dl['Confirmed'])
        plt.plot(dl['Date'], dl['Confirmed'])
        plt.plot(dl['Date'], dl['Confirmed'])
        plt.plot(dl['Date'], dl['Confirmed'])
        plt.plot(dl['Date'], dl['Confirmed'])
        plt.plot(dl['Date'], dl['Confirmed'])
        plt.plot(dl['Date'], dl['Confirmed'])
        plt.plot(dl['Date'], dl['Confirmed'])
        plt.plot(dl['Date'], dl['Confirmed'])
        plt.plot(dl['Date'], dl['Confirmed'])
        plt.plot(dl['Date'], dl['Confirmed'])
        plt.plot(dl['Date'], dl['Confirmed'])
        plt.plot(dl['Date'], dl['Confirmed'])
        plt.plot(dl['Date'], dl['Confirmed'])
        plt.plot(dl['Date'], dl['Confirmed'])
        plt.plot(dl['Date'], dl['Confirmed'])
        plt.plot(dl['Date'], dl['Confirmed'])
        plt.legend([nlist[0], nlist[1],nlist[2]])
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(e)

alldata()