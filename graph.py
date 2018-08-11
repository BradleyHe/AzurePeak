import pandas as pd

def getStats(df, statsInterval):
	if(readingsInterval % 100 != 0):
		return "error, interval must be in hundreds of seconds"

	minTime = df.index.values.min()
	maxTime = df.index.values.max()

	time = []
	minCores = []
	maxCores = []
	percentileCores = []
	delays = []
	mean = []

	for num in range(minTime, maxTime, statsInterval):
		interval = df.loc[num : num + statsInterval - 1, 'cores']
		percentile = interval.quantile([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])

		time.append(num)
		minCores.append(interval.min())
		maxCores.append(interval.max())
		mean.append(interval.mean())
		percentileCores.append(percentile.to_dict())
		delays.append(df.loc[num : num + statsInterval, 'delays'].sum())

	stats = pd.DataFrame(index = time, columns = ['minimum', 'maximum', 'percentiles'])
	stats['minimum'] = minCores
	stats['maximum'] = maxCores
	stats['percentiles'] = percentileCores
	stats['delays'] = delays
	stats['mean'] = mean

	return stats

def moving(data, start, end, window, delay, stdMultiplier, statsInterval):
	if(start % 100 != 0):
		return "error: start must be in hundreds of seconds"
	if(end % 100 != 0):
		return "error: end must be in hundreds of seconds"
	if(delay % 100 != 0):
		return "error: delay must be in hundreds of seconds"

	list = []
	constant = 0
	data.sort_values('vmcreated', inplace = True)

	# determine how many cores are constant during the time period in which we are graphing
	# this will shave down runtime
	for index, vm in data.iterrows():
		if(vm['vmcreated'] > start):
			break

		if(vm['vmcreated'] <= start and vm['vmdeleted'] >= end):
			constant += vm['vmcorecount']

	# add all necessary rows
	for num in range(start, end + 1, 100):
		list.append([num, constant, 0])

	# create dataframe from list
	df = pd.DataFrame(list, columns = ['time', 'cores', 'delays'])
	df = df.set_index('time')

	for index, vm in data.iterrows():
		vmCreateTime = vm['vmcreated']
		vmDeleteTime = vm['vmdeleted']

		if(vmCreateTime > end):
			break

		# ignore vms that are constant throughout time period, we have already accounted for them
		if(vmCreateTime <= start and vmDeleteTime >= end):
			continue

		df['MA'] = df.iloc[start:vmCreateTime, 0].rolling(window).mean()
		df['STD'] = df.iloc[start:vmCreateTime, 0].rolling(window).std()
		df['limit'] = df['MA'] + df['STD'] * stdMultiplier

		if(df.at[vmCreateTime, 'cores'] > df.at[vmCreateTime, 'limit']):
			df.at[vmCreateTime, 'delays'] += vm['vmcorecount']
			vmCreateTime += delay
			vmDeleteTime += delay

		min = vmCreateTime if vmCreateTime > start else start
		max = vmDeleteTime if vmDeleteTime < end else end

		# cumulatively add vmcorecount to the time period in which the vm is active
		for num in range(min, max, 100):
			df.at[num, 'cores'] += vm['vmcorecount']

	df.sort_index(inplace = True)

	stats = getStats(df)
	stats.to_csv('stats/moving/moving_{0}to{1}_window={2}_delay={3}_multiplier={4}_statsInterval={5}.csv'.format(start, end, window, delay, stdMultiplier, statsInterval))
	df.to_csv('data/moving/moving_{0}to{1}_window={2}_delay={3}_multiplier={4}.csv'.format(start, end, window, delay, stdMultiplier))

def interval(data, start, end, interval, delay):
	if(start % 100 != 0):
		return "error: start must be in hundreds of seconds"
	if(end % 100 != 0):
		return "error: end must be in hundreds of seconds"
	if(interval % 100 != 0):
		return "error: interval must be in hundreds of seconds"
	if(delay % 100 != 0):
		return "error: delay must be in hundreds of seconds"

	list = []
	constant = 0;
	data.sort_values('vmcreated', inplace = True)
	selectedData = data.query('0 <= vmcreated <= {}'.format(end))

	# determine how many cores are constant during the time period in which we are graphing
	# this will shave down runtime
	for index, vm in data.iterrows():
		if(vm['vmcreated'] > start):
			break

		if(vm['vmcreated'] <= start and vm['vmdeleted'] >= end):
			constant += vm['vmcorecount']

	# add all necessary rows
	for num in range(start, end + 1, 100):
		list.append([num, constant, 0])

	# create dataframe from list
	df = pd.DataFrame(list, columns = ['time', 'cores', 'delays'])
	df = df.set_index('time')

	for index, vm in data.iterrows():
		vmCreateTime = vm['vmcreated']
		vmDeleteTime = vm['vmdeleted']

		if(vmCreateTime > end):
			break

		# ignore vms that are constant throughout time period, they are already accounted for
		if(vmCreateTime <= start and vmDeleteTime >= end):
			continue

		# if creation time is on an interval, delay
		if((vmCreateTime - start) % interval == 0 and vmCreateTime != start):
			df.at[vmCreateTime, 'delays'] += 1
			vmCreateTime += delay
			vmDeleteTime += delay

		min = vmCreateTime if vmCreateTime > start else start
		max = vmDeleteTime if vmDeleteTime < end else end

		# cumulatively add vmcorecount to the time period in which the vm is active
		for num in range(min, max, 100):
			df.at[num, 'cores'] += vm['vmcorecount']

	df.sort_index(inplace = True)

	stats = getStats(df)
	stats.to_csv('stats/moving/moving_{0}to{1}interval={2}_delay={3}_statsInterval={4}.csv'.format(start, end, interval, delay, statsInterval))
	df.to_csv('data/moving/moving_{0}to{1}_interval={2}_delay={3}.csv'.format(start, end, interval, delay))

def globalMax(data, start, end, window, delay, percentage):
	maximum = 0
	minimum = 1000000

	if(start % 100 != 0):
		return "error: start must be in hundreds of seconds"
	if(end % 100 != 0):
		return "error: end must be in hundreds of seconds"
	if(delay % 100 != 0):
		return "error: delay must be in hundreds of seconds"

	list = []
	constant = 0
	data.sort_values('vmcreated', inplace = True)
	selectedData = data.query('0 <= vmcreated <= {}'.format(end))

	# determine how many cores are constant during the time period in which we are graphing
	# this will shave down runtime
	for index, vm in data.iterrows():
		if(vm['vmcreated'] > start):
			break

		if(vm['vmcreated'] <= start and vm['vmdeleted'] >= end):
			constant += vm['vmcorecount']

	# add all necessary rows
	for num in range(start, end + 1, 100):
		list.append([num, constant, 0])

	# create dataframe from list
	df = pd.DataFrame(list, columns = ['time', 'cores', 'delays'])
	df = df.set_index('time')

	newList = []
	currentTime = start

	for index, vm in data.iterrows():
		vmCreateTime = vm['vmcreated']
		vmDeleteTime = vm['vmdeleted']

		if(vmCreateTime > end):
			break

		if(currentTime < vmCreateTime):
			if(currentTime == start):
				minimum = df.at[start, 'cores']
				maximum = df.at[start, 'cores']
				for num in range(currentTime, vmCreateTime, 100):
					newList.append(minimum + (maximum - minimum) * percentage)

			else:
				for num in range(currentTime, vmCreateTime, 100):
					newList.append(minimum + (maximum - minimum) * percentage)

			minimum = df.at[vmCreateTime, 'cores'] if minimum > df.at[vmCreateTime, 'cores'] else minimum
			maximum = df.at[vmCreateTime, 'cores'] if maximum < df.at[vmCreateTime, 'cores'] else maximum
			currentTime = vmCreateTime

		# ignore vms that are constant throughout time period, we have already accounted for them
		if(vmCreateTime == start and vmDeleteTime >= end):
			continue

		# calculate moving avg
		df['MA'] = df.iloc[start:vmCreateTime, 0].rolling(window).mean()

		# if current core count is greater than global maximum, delay
		if(df.at[vmCreateTime, 'MA'] > minimum + (maximum - minimum) * percentage):
			df.at[vmCreateTime, 'delays'] += 1
			vmCreateTime += delay
			vmDeleteTime += delay

		min = vmCreateTime if vmCreateTime > start else start
		max = vmDeleteTime if vmDeleteTime < end else end

		# cumulatively add vmcorecount to the time period in which the vm is active
		for num in range(min, max, 100):
			df.at[num, 'cores'] += vm['vmcorecount']

	for num in range(len(newList), int((end - start) / 100) + 1):
		newList.append(minimum + (maximum - minimum) * percentage)

	df.sort_index(inplace = True)
	df['max'] = newList

	stats = getStats(df)
	stats.to_csv('stats/moving/moving_{0}to{1}_window={2}_delay={3}_multiplier={4}_statsInterval={}.csv'.format(start, end, window, delay, percentage, statsInterval))
	df.to_csv('data/moving/moving_{0}to{1}_window={2}_delay={3}_multiplier={4}.csv'.format(start, end, window, delay, percentage))
