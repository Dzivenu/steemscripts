import urllib.request
import json
import matplotlib.pyplot as plt
fp = urllib.request.urlopen("https://steemdb.com/api/rewards")
mybytes = fp.read()

jesta = mybytes.decode("utf8")
fp.close()

data = json.loads(jesta)

day = []
sbd = []
steem = []
vests = []
daynum = 0
for days in data:
    daynum=daynum+1
    day.append(daynum)
    sbd.append(days["sbd"])
    steem.append(days["steem"])
    vests.append(days["vest"]/1000)

plt.plot(day, sbd, '-b')
plt.plot(day, steem, '-g')
plt.plot(day, vests, '-y')
plt.legend(['SBD', 'STEEM', 'VESTS/1000'], loc='upper left')
plt.ylabel('Rewards')
plt.xlabel('Days')
plt.show()
