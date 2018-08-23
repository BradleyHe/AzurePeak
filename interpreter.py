import pandas as pd
import matplotlib.pyplot as plt

start = 0
end = 172800
statsInterval = 3600
raw = pd.read_csv('stats/moving/moving_0to172800_window=10_delay=0_multiplier=1_statsInterval={}.csv'.format(statsInterval), index_col = 0)
globalMin = 321181
rawDiff = raw['maximum'] - raw['minimum']
globalMinDiff = raw['maximum'] - globalMin

# moving
window10mult1 = pd.read_csv('stats/moving/moving_0to172800_window=10_delay=300_multiplier=1_statsInterval={}.csv'.format(statsInterval), index_col = 0)
window10mult2 = pd.read_csv('stats/moving/moving_0to172800_window=10_delay=300_multiplier=2_statsInterval={}.csv'.format(statsInterval), index_col = 0)
window10mult3 = pd.read_csv('stats/moving/moving_0to172800_window=10_delay=300_multiplier=3_statsInterval={}.csv'.format(statsInterval), index_col = 0)
window10multn1 = pd.read_csv('stats/moving/moving_0to172800_window=10_delay=300_multiplier=-1_statsInterval={}.csv'.format(statsInterval), index_col = 0)
window10multn2 = pd.read_csv('stats/moving/moving_0to172800_window=10_delay=300_multiplier=-2_statsInterval={}.csv'.format(statsInterval), index_col = 0)
window10multn3 = pd.read_csv('stats/moving/moving_0to172800_window=10_delay=300_multiplier=-3_statsInterval={}.csv'.format(statsInterval), index_col = 0)

window20mult1 = pd.read_csv('stats/moving/moving_0to172800_window=20_delay=300_multiplier=1_statsInterval={}.csv'.format(statsInterval), index_col = 0)
window20mult2 = pd.read_csv('stats/moving/moving_0to172800_window=20_delay=300_multiplier=2_statsInterval={}.csv'.format(statsInterval), index_col = 0)
window20mult3 = pd.read_csv('stats/moving/moving_0to172800_window=20_delay=300_multiplier=3_statsInterval={}.csv'.format(statsInterval), index_col = 0)
window20multn1 = pd.read_csv('stats/moving/moving_0to172800_window=20_delay=300_multiplier=-1_statsInterval={}.csv'.format(statsInterval), index_col = 0)
window20multn2 = pd.read_csv('stats/moving/moving_0to172800_window=20_delay=300_multiplier=-2_statsInterval={}.csv'.format(statsInterval), index_col = 0)
window20multn3 = pd.read_csv('stats/moving/moving_0to172800_window=20_delay=300_multiplier=-3_statsInterval={}.csv'.format(statsInterval), index_col = 0)

window50mult1 = pd.read_csv('stats/moving/moving_0to172800_window=50_delay=300_multiplier=1_statsInterval={}.csv'.format(statsInterval), index_col = 0)
window50mult2 = pd.read_csv('stats/moving/moving_0to172800_window=50_delay=300_multiplier=2_statsInterval={}.csv'.format(statsInterval), index_col = 0)
window50mult3 = pd.read_csv('stats/moving/moving_0to172800_window=50_delay=300_multiplier=3_statsInterval={}.csv'.format(statsInterval), index_col = 0)
window50multn1 = pd.read_csv('stats/moving/moving_0to172800_window=50_delay=300_multiplier=-1_statsInterval={}.csv'.format(statsInterval), index_col = 0)
window50multn2 = pd.read_csv('stats/moving/moving_0to172800_window=50_delay=300_multiplier=-2_statsInterval={}.csv'.format(statsInterval), index_col = 0)
window50multn3 = pd.read_csv('stats/moving/moving_0to172800_window=50_delay=300_multiplier=-3_statsInterval={}.csv'.format(statsInterval), index_col = 0)

# interval
interval900 = pd.read_csv('stats/interval/interval_0to172800_interval=900_delay=300_statsInterval={}.csv'.format(statsInterval), index_col = 0)
interval1800 = pd.read_csv('stats/interval/interval_0to172800_interval=1800_delay=300_statsInterval={}.csv'.format(statsInterval), index_col = 0)
interval2700 = pd.read_csv('stats/interval/interval_0to172800_interval=2700_delay=300_statsInterval={}.csv'.format(statsInterval), index_col = 0)
interval3600 = pd.read_csv('stats/interval/interval_0to172800_interval=3600_delay=300_statsInterval={}.csv'.format(statsInterval), index_col = 0)
interval7200 = pd.read_csv('stats/interval/interval_0to172800_interval=7200_delay=300_statsInterval={}.csv'.format(statsInterval), index_col = 0)

# global max
percentage60 = pd.read_csv('stats/globalMax/globalMax_0to172800_window=10_delay=300_percentage=0.6_statsInterval={}.csv'.format(statsInterval), index_col = 0)
percentage70 = pd.read_csv('stats/globalMax/globalMax_0to172800_window=10_delay=300_percentage=0.7_statsInterval={}.csv'.format(statsInterval), index_col = 0)
percentage80 = pd.read_csv('stats/globalMax/globalMax_0to172800_window=10_delay=300_percentage=0.8_statsInterval={}.csv'.format(statsInterval), index_col = 0)
percentage85 = pd.read_csv('stats/globalMax/globalMax_0to172800_window=10_delay=300_percentage=0.85_statsInterval={}.csv'.format(statsInterval), index_col = 0)
percentage90 = pd.read_csv('stats/globalMax/globalMax_0to172800_window=10_delay=300_percentage=0.9_statsInterval={}.csv'.format(statsInterval), index_col = 0)


df = pd.DataFrame(index = raw.index)

# performance calculator (finds the percentage of time where the method was effective)
statsList = (window10mult1, window10mult2, window10mult3, window10multn1, window10multn2, window10multn3, window20mult1, window20mult2, window20mult3, window20multn1, window20multn2, window20multn3, 
	 window50mult1, window50mult2, window50mult3, window50multn1, window50multn2, window50multn3, interval900, interval1800, interval2700, interval3600, interval7200, percentage60, percentage70, percentage80, percentage85, percentage90)

split = "window10mult1, window10mult2, window10mult3, window10multn1, window10multn2, window10multn3, window20mult1, window20mult2, window20mult3, window20multn1, window20multn2, window20multn3, \
	 window50mult1, window50mult2, window50mult3, window50multn1, window50multn2, window50multn3, interval900, interval1800, interval2700, interval3600, interval7200, percentage60, percentage70, percentage80, percentage85, percentage90".split(', ')

list = []

for stats in statsList:
	lesser = 0

	for index, row in stats.iterrows():
		if row['maximum'] < raw.loc[index]['maximum']:
			lesser += 1
		if row['minimum'] < raw.loc[index]['minimum']:
			lesser -= 1

	list.append(lesser)

statsDict = dict(zip(split, list))
sortedValues = sorted(statsDict.values(), reverse = True)
sortedKeys = sorted(statsDict, key = statsDict.get, reverse = True)

output = open('lessermaximum-greatermaximum.txt', 'a+')

for num in range(0, 28):
	output.write(sortedKeys[num] + ': ' + str(sortedValues[num]) + '\n')

# moving method comparisons --------------------------------------------------------------
# differences of local max of 1h - local min of 1h
# positive indicates lesser peaks and dips, negative indicates greater peaks and dips
# df['10n1'] = rawDiff - (window10multn1['maximum'] - window10multn1['minimum'])
# df['10p1'] = rawDiff - (window10mult1['maximum'] - window10mult1['minimum'])
# df['20p1'] = rawDiff - (window20mult1['maximum'] - window20mult1['minimum'])
# df['20n1'] = rawDiff - (window20multn1['maximum'] - window20multn1['minimum'])
# df['50p1'] = rawDiff - (window50mult1['maximum'] - window50mult1['minimum'])
# df['50n1'] = rawDiff - (window50multn1['maximum'] - window50multn1['minimum'])

# differences of local maximums 10 to 50
# df['10n1'] = raw['maximum'] - window10multn1['maximum']
# df['10p1'] = raw['maximum'] - window10mult1['maximum']
# df['10n2'] = raw['maximum'] - window10multn2['maximum']
# df['10p2'] = raw['maximum'] - window10mult2['maximum']
# df['20p1'] = raw['maximum'] - window20mult1['maximum']
# df['20n1'] = raw['maximum'] - window20multn1['maximum']
# df['20p2'] = raw['maximum'] - window20mult2['maximum']
# df['20n2'] = raw['maximum'] - window20multn2['maximum']
# df['50p1'] = raw['maximum'] - window50mult1['maximum']
# df['50n1'] = raw['maximum'] - window50multn1['maximum']
# df['50p2'] = raw['maximum'] - window50mult2['maximum']
# df['50n2'] = raw['maximum'] - window50multn2['maximum']
# filename = 'results/localmax-localmax/moving10to50_localmax-localmax_results_statsInterval={}'.format(statsInterval)

# 10 to 20
# df['10n1'] = raw['maximum'] - window10multn1['maximum']
# df['10p1'] = raw['maximum'] - window10mult1['maximum']
# df['10n2'] = raw['maximum'] - window10multn2['maximum']
# df['10p2'] = raw['maximum'] - window10mult2['maximum']
# df['20p1'] = raw['maximum'] - window20mult1['maximum']
# df['20n1'] = raw['maximum'] - window20multn1['maximum']
# df['20p2'] = raw['maximum'] - window20mult2['maximum']
# df['20n2'] = raw['maximum'] - window20multn2['maximum']
# filename = 'results/moving10to20_localmax-localmax_results_statsInterval={}'.format(statsInterval)

# 10
# df['10n1'] = raw['maximum'] - window10multn1['maximum']
# df['10p1'] = raw['maximum'] - window10mult1['maximum']
# df['10n2'] = raw['maximum'] - window10multn2['maximum']
# df['10p2'] = raw['maximum'] - window10mult2['maximum']
# filename = 'results/moving10_localmax-localmax_results_statsInterval={}'.format(statsInterval)

# maximum
# df['raw'] = raw['maximum']
# df['10n2max'] = window10multn2['maximum']
# df['10n1max'] = window10multn1['maximum']
# df['101max'] = window10mult1['maximum']
# df['102max'] = window10mult2['maximum']
# df['20n2max'] = window20multn2['maximum']
# df['20n1max'] = window20multn1['maximum']
# df['201max'] = window20mult1['maximum']
# df['202max'] = window20mult2['maximum']

# mean
# (50n2 is not included since it is basically the raw data but shifted over 5 minutes)
# df['10n1'] = window10multn1['mean']
# df['10p1'] = window10mult1['mean']
# df['10n2'] = window10multn2['mean']
# df['10p2'] = window10mult2['mean']
# df['20p1'] = window20mult1['mean']
# df['20n1'] = window20multn1['mean']
# df['20p2'] = window20mult2['mean']
# df['20n2'] = window20multn2['mean']
# df['50p1'] = window50mult1['mean']
# df['50n1'] = window50multn1['mean']
# df['50p2'] = window50mult2['mean']
# filename = 'results/moving_mean_results_statsInterval={}'.format(statsInterval)
# ----------------------------------------------------------------------------------------

# interval comparison --------------------------------------------------------------
# differences of local maximums
# df['interval900'] = raw['maximum'] - interval900['maximum']
# df['interval1800'] = raw['maximum'] - interval1800['maximum']
# df['interval2700'] = raw['maximum'] - interval2700['maximum']
# df['interval3600'] = raw['maximum'] - interval3600['maximum']
# df['interval7200'] = raw['maximum'] - interval7200['maximum']
# filename = 'results/interval_localmax-localmax_results_statsInterval={}'.format(statsInterval)

# mean
# df['interval900'] = interval900['mean']
# df['interval1800'] = interval1800['mean']
# df['interval2700'] = interval2700['mean']
# df['interval3600'] = interval3600['mean']
# df['interval7200'] = interval7200['mean']
# filename = 'results/interval_mean_results_statsInterval={}'.format(statsInterval)
# ----------------------------------------------------------------------------------------

# global max comparison --------------------------------------------------------------
# differences of local maximums
# df['percentage90'] = raw['maximum'] - percentage90['maximum']
# df['percentage85'] = raw['maximum'] - percentage85['maximum']
# df['percentage80'] = raw['maximum'] - percentage80['maximum']
# df['percentage70'] = raw['maximum'] - percentage70['maximum']
# df['percentage60'] = raw['maximum'] - percentage60['maximum']
# filename = 'results/localmax-localmax/global_localmax-localmax_results_statsInterval={}'.format(statsInterval)

# mean
# df['percentage90'] = percentage90['mean']
# df['percentage85'] = percentage85['mean']
# df['percentage80'] = percentage80['mean']
# df['percentage70'] = percentage70['mean']
# df['percentage60'] = percentage60['mean']
# filename = 'results/global_mean_results_statsInterval={}'.format(statsInterval)

# maximum
# df['percentage90'] = percentage90['maximum']
# df['percentage85'] = percentage85['maximum']
# df['percentage80'] = percentage80['maximum']
# df['percentage70'] = percentage70['maximum']
# df['percentage60'] = percentage60['maximum']
# filename = 'results/global_localmax_results_statsInterval={}'.format(statsInterval)
# ----------------------------------------------------------------------------------------

# multiple methods comparison --------------------------------------------------------------
# differences of local maximums
df['10p1'] = raw['maximum'] - window10mult1['maximum']
df['10p2'] = raw['maximum'] - window10mult2['maximum']
df['50p1'] = raw['maximum'] - window20mult1['maximum']
# df['50p2'] = raw['maximum'] - window20mult2['maximum']
# df['percentage90'] = raw['maximum'] - percentage90['maximum']
# df['percentage70'] = raw['maximum'] - percentage70['maximum']
# df['interval3600'] = raw['maximum'] - interval3600['maximum']
# df['interval7200'] = raw['maximum'] - interval7200['maximum']
# filename = 'results/localmax-localmax/moving+globalmax+interval_localmax-localmax_results_statsInterval={}'.format(statsInterval)

# mean
# df['10p1'] = window10mult1['mean']
# df['10p2'] = window10mult2['mean']
# df['50p1'] = window20mult1['mean']
# df['50p2'] = window20mult2['mean']
# df['percentage90'] = percentage90['mean']
# df['percentage70'] = percentage70['mean']
# df['interval3600'] = interval3600['mean']
# df['interval7200'] = interval7200['mean']
# filename = 'results/mean/moving+globalmax+interval_mean_results_statsInterval={}'.format(statsInterval)

# mean - mean
# df['10p1'] = raw['mean'] - window10mult1['mean']
# df['10p2'] = raw['mean'] - window10mult2['mean']
# df['50p1'] = raw['mean'] - window20mult1['mean']
# df['50p2'] = raw['mean'] - window20mult2['mean']
# df['percentage90'] = raw['mean'] - percentage90['mean']
# df['percentage70'] = raw['mean'] - percentage70['mean']
# df['interval3600'] = raw['mean'] - interval3600['mean']
# df['interval7200'] = raw['mean'] - interval7200['mean']
# filename = 'results/moving+globalmax+interval_mean-mean_results_statsInterval={}'.format(statsInterval)
# ----------------------------------------------------------------------------------------

# minValue = []
# maxValue = []

# # i convert the numpy list here to a tuple in order to see the value counts, it is fine if you use the commented block instead (just comment out the print statements)
# for index, data in df.iterrows():
# 	minValue.append(tuple(df.columns[(df == data.min()).loc[index]].tolist()))
# 	maxValue.append(tuple(df.columns[(df == data.max()).loc[index]].tolist()))
# 	# minValue.append(df.columns[(df == data.min()).loc[index]].tolist())
# 	# maxValue.append(df.columns[(df == data.max()).loc[index]].tolist())

# df['min'] = minValue
# df['max'] = maxValue

# fig_size = plt.rcParams["figure.figsize"]
# fig_size[0] = 12
# plt.rcParams["figure.figsize"] = fig_size
# df.plot()
# plt.savefig(filename + '.jpg')
# plt.show()

# print(df['min'].value_counts())
# print(df['max'].value_counts())
# df.to_csv(filename + '.csv')
