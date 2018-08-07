import pandas as pd
import graph
import matplotlib.pyplot as plt

start = 0
end = 21600
window = 10
interval = 900
delay = 300
percentage = 0.5
stdMultiplier = -3

headers = ['vmid','subscriptionid','deploymentid','vmcreated', 'vmdeleted', 'maxcpu', 'avgcpu', 'p95maxcpu', 'vmcategory', 'vmcorecount', 'vmmemory']
data_path = 'vmtable.csv'

data = pd.read_csv(data_path,header=None, index_col=False,names=headers,delimiter=',')
vmdata = data[['vmcreated', 'vmdeleted', 'vmcorecount']]
vmdata = vmdata.sort_values('vmcreated')

# for moving avg
# graph.moving(vmdata, start, end, window, delay, stdMultiplier)
# df = pd.read_csv('data/moving/moving_{0}to{1}_window={2}_delay={3}_multiplier={4}.csv'.format(start, end, window, delay, stdMultiplier))
# df.set_index("time", inplace=True)
# df.drop(df.tail(1).index, inplace=True)
# df.drop(['STD', 'MA', 'delays'], axis=1).plot(ylim = (321000, 325000))
# plt.savefig('graphs/moving/moving_{0}to{1}_window={2}_delay={3}_multiplier={4}.jpg'.format(start, end, window, delay, stdMultiplier))
# plt.show()

# for set interval
# graph.interval(vmdata, start, end, interval, delay)
# df = pd.read_csv('data/interval/interval_{0}to{1}_interval={2}_delay={3}.csv'.format(start, end, interval, delay))
# df.set_index('time', inplace=True)
# df.drop(df.tail(1).index, inplace=True)
# df.drop(['delays'], axis = 1).plot(ylim = (321000, 325000))
# plt.savefig('graphs/interval/interval_{0}to{1}_interval={2}_delay={3}.jpg'.format(start, end, interval, delay))
# plt.show()

# for global maximum
graph.globalMax(vmdata, start, end, window, delay, percentage)
df = pd.read_csv('data/globalMax/globalMax_{0}to{1}_window={2}_delay={3}_percentage={4}.csv'.format(start, end, window, delay, percentage))
df.set_index('time', inplace=True)
df.drop(df.tail(1).index, inplace=True)
df.drop(['delays'], axis = 1).plot(ylim = (321000, 325000))
plt.savefig('graphs/globalMax/globalMax_{0}to{1}_window={2}_delay={3}_percentage={4}.jpg'.format(start, end, window, delay, percentage))
plt.show()