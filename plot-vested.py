import urllib.request
import json
import matplotlib.pyplot as plt
fp = urllib.request.urlopen("https://steemdb.com/api/percentage")
mybytes = fp.read()

jesta = mybytes.decode("utf8")
fp.close()

data = json.loads(jesta)
data = json.dumps(data, sort_keys=True)
data = json.loads(data)
data4 = json.dumps(data, sort_keys=True)
keys = []
values = []
for key in data:
    keys.append(key)
    values.append(data[key])
print(data4)
plt.plot(keys, values, '-b', zorder=10)
plt.ylabel('\% vested')
plt.xlabel('timestamp')
plt.show()
