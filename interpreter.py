import pandas as pd
import matplotlib.pyplot as plt

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

df = pd.DataFrame(index = raw.index)

# moving method comparisons --------------------------------------------------------------
# differences of local max of 1h - local min of 1h
df['10n1'] = rawDiff - (window10multn1['maximum'] - window10multn1['minimum'])
df['10p1'] = rawDiff - (window10mult1['maximum'] - window10mult1['minimum'])
df['20p1'] = rawDiff - (window20mult1['maximum'] - window20mult1['minimum'])
df['20n1'] = rawDiff - (window20multn1['maximum'] - window20multn1['minimum'])
df['50p1'] = rawDiff - (window50mult1['maximum'] - window50mult1['minimum'])
df['50n1'] = rawDiff - (window50multn1['maximum'] - window50multn1['minimum'])


# ratio of local max of 1h - local min of 1h
# df['10n2'] = (window10multn2['maximum'] - window10multn2['minimum']) / rawDiff
# df['10n1'] = (window10multn1['maximum'] - window10multn1['minimum']) / rawDiff
# df['10p1'] = (window10mult1['maximum'] - window10mult1['minimum']) / rawDiff
# df['10p2'] = (window10mult2['maximum'] - window10mult2['minimum']) / rawDiff
# df['20n2'] = (window20multn2['maximum'] - window20multn2['minimum']) / rawDiff
# df['20n1'] = (window20multn1['maximum'] - window20multn1['minimum']) / rawDiff
# df['20p1'] = (window20mult1['maximum'] - window20mult1['minimum']) / rawDiff
# df['20p2'] = (window20mult2['maximum'] - window20mult2['minimum']) / rawDiff

# ratio of local max of 1h - global min of 1h
# df['10n2'] = (window10multn2['maximum'] - globalMin) / globalMinDiff
# df['10n1'] = (window10multn1['maximum'] - globalMin) / globalMinDiff
# df['10p1'] = (window10mult1['maximum'] - globalMin) / globalMinDiff
# df['10p2'] = (window10mult2['maximum'] - globalMin) / globalMinDiff
# df['20n2'] = (window20multn2['maximum'] - globalMin) / globalMinDiff
# df['20n1'] = (window20multn1['maximum'] - globalMin) / globalMinDiff
# df['20p1'] = (window20mult1['maximum'] - globalMin) / globalMinDiff
# df['20p2'] = (window20mult2['maximum'] - globalMin) / globalMinDiff

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
# ----------------------------------------------------------------------------------------

# multiple methods comparison --------------------------------------------------------------

# ----------------------------------------------------------------------------------------

minValue = []
maxValue = []

# i convert the numpy list here to a tuple in order to see the value counts, it is fine if you use the commented block instead
for index, data in df.iterrows():
	minValue.append(tuple(df.columns[(df == data.min()).loc[index]].tolist()))
	maxValue.append(tuple(df.columns[(df == data.max()).loc[index]].tolist()))
	# minValue.append(df.columns[(df == data.min()).loc[index]].tolist())
	# maxValue.append(df.columns[(df == data.max()).loc[index]].tolist())

df['min'] = minValue
df['max'] = maxValue

fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 12
plt.rcParams["figure.figsize"] = fig_size
df.plot()
plt.savefig('results/window10to50_n1to1_localmax-localmax_results_statsInterval={}.jpg'.format(statsInterval))
plt.show()

print(df['min'].value_counts())
print(df['max'].value_counts())
df.to_csv('results/window10to50_n1to1_localmax-localmax_results_statsInterval={}.csv'.format(statsInterval))