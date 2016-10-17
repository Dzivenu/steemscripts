import urllib.request
import json
import matplotlib.pyplot as plt
fp = urllib.request.urlopen("https://steemdb.com/api/supply")
mybytes = fp.read()

jesta = mybytes.decode("utf8")
fp.close()

data = json.loads(jesta)

day = []
sbd = []
sbd_savings = []
steem = []
steem_savings = []
vests = []
daynum = 0
for days in data:
    daynum=daynum+1
    day.append(daynum)
    sbd.append(days["sbd"])
    sbd_savings.append(days["sbd_savings"])
    steem.append(days["steem"])
    steem_savings.append(days["steem_savings"])
    vests.append(days["vests"])

plt.plot(day, sbd, '-b')
#plt.plot(day, sbd_savings, '-r')
plt.plot(day, steem, '-g')
#plt.plot(day, steem_savings, '-k')
#plt.plot(day, vests, '-y')
#plt.legend(['SBD_SAVINGS', 'STEEM_SAVINGS'], loc='upper left')
plt.legend(['SBD', 'STEEM'], loc='upper left')
plt.ylabel('Supply')
plt.xlabel('Days')
plt.show()
