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
        
        plt.title('Confirmed COVID Cases DATA')
        plt.xlabel('Dates')
        plt.ylabel('Number')
        plt.plot(kl['Date'], kl['Confirmed'])
        plt.plot(tl['Date'], tl['Confirmed'])
        plt.plot(dl['Date'], dl['Confirmed'])
        plt.plot(rj['Date'], rj['Confirmed'])
        plt.plot(up['Date'], up['Confirmed'])
        plt.plot(hy['Date'], hy['Confirmed'])
        plt.plot(ld['Date'], ld['Confirmed'])
        plt.plot(tn['Date'], tn['Confirmed'])
        plt.plot(kt['Date'], kt['Confirmed'])
        plt.plot(mh['Date'], mh['Confirmed'])
        plt.plot(pb['Date'], pb['Confirmed'])
        plt.plot(jk['Date'], jk['Confirmed'])
        plt.plot(ap['Date'], ap['Confirmed'])
        plt.plot(uk['Date'], uk['Confirmed'])
        plt.plot(od['Date'], od['Confirmed'])
        plt.plot(wb['Date'], wb['Confirmed'])
        plt.plot(py['Date'], py['Confirmed'])
        plt.plot(ch['Date'], ch['Confirmed'])
        plt.plot(cg['Date'], cg['Confirmed'])
        plt.plot(gj['Date'], gj['Confirmed'])
        plt.plot(hp['Date'], hp['Confirmed'])
        plt.plot(mp['Date'], mp['Confirmed'])
        plt.plot(br['Date'], br['Confirmed'])
        plt.plot(mn['Date'], mn['Confirmed'])
        plt.plot(mz['Date'], mz['Confirmed'])
        plt.plot(nc['Date'], nc['Confirmed'])
        plt.plot(ga['Date'], ga['Confirmed'])
        plt.plot(am['Date'], am['Confirmed'])
        plt.legend([
            nlist[0], nlist[1],nlist[2],nlist[3],nlist[4],nlist[5],nlist[6],nlist[7],nlist[8],nlist[9],nlist[10],nlist[11],nlist[12],nlist[13],nlist[14],nlist[15],nlist[16],nlist[17],nlist[18],nlist[19],nlist[20],nlist[21],nlist[22],nlist[23],nlist[24],nlist[25],nlist[26],nlist[28]
        ])
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(e)

