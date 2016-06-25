

class course:
	def __init__(self, name, meet_times):
		#meet_times is ['mon', time_range] (day is first three letters)
		self.name = name
		self.meet_times = meet_times
		
	def conflict(self, other):
	
	def __str__(self):
		ret = self.name + " " +



class time:
	def __init__(self, hour, minutes, am_or_pm):
		"""
		am_or_pm is 'am' or 'pm', all others are ints
		"""
		hours = hour if am_or_pm=='am' else hour + 12
		self.time_in_mins = minutes +  hours*60
		self.toprint = [hour, minutes]
	def __lt__(self, other):
		# self is a time before other iff
		return self.time_in_mins < other.time_in_mins
	def __gt__(self, other):
		# self is a time after other
		return self.time_in_mins > other.time_in_mins
	def __eq__(self, other):
		return self.time_in_mins == other.time_in_mins
	def __str__(self):
		hour = self.toprint[0]
		hour = hour if hour < 13 else hour - 12
		return str(hour) + ":" + str(self.toprint[1])
class time_range:
	def __init__(self, start, end):
		assert(all([type(i) == time for i in [start, end]]))
		assert(start < end)
		self.time_range = [start, end]
	def in_range(self, time_object):
		return time_object == self.time_range[0] or time_object == self.time_range[1] or \
			(time_object > self.time_range[0] and time_object < self.time_range[1])
	def overlap(self, other):
		return self.in_range(other.time_range[0]) or self.in_range(other.time_range[1])
	
	