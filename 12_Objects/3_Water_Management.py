class WaterPoint:
	def __init__(self, location, capacity_liters):
		self.location = location
		self.capacity_liters = capacity_liters
		self.current_level = capacity_liters
		self.daily_usage = []
		self.users_served = 0
	
	def dispense_water(self, liters):
		if liters <= self.current_level:
			self.current_level -= liters
			self.users_served += 1
			return True
		else:
			return False
	
	def refill(self, liters=None):
		if liters is None:
			# Full refill
			refill_amount = self.capacity_liters - self.current_level
			self.current_level = self.capacity_liters
		else:
			# Partial refill
			refill_amount = liters
			self.current_level = min(self.capacity_liters, self.current_level + liters)
		return refill_amount
	
	def record_daily_usage(self):
		# Record yesterday's usage
		used = self.capacity_liters - self.current_level
		self.daily_usage.append(used)
		# Reset for new day
		self.current_level = self.capacity_liters
		self.users_served = 0
		return used
	
	def average_daily_usage(self):
		if not self.daily_usage:
			return 0
		return sum(self.daily_usage) / len(self.daily_usage)
	
	def status_report(self):
		percentage_full = (self.current_level / self.capacity_liters) * 100
		print(f"Water Point Status: {self.location}")
		print(f"Capacity: {self.capacity_liters} liters")
		print(f"Current Level: {self.current_level:.1f} liters ({percentage_full:.1f}%)")
		print(f"Users Served Today: {self.users_served}")
		print(f"Average Daily Usage: {self.average_daily_usage():.1f} liters")
		if self.daily_usage:
			print(f"Usage History: {', '.join(str(int(u)) for u in self.daily_usage)} liters")


class NeighborhoodWaterSystem:
	def __init__(self, name):
		self.name = name
		self.water_points = {}
	
	def add_water_point(self, location, capacity):
		water_point = WaterPoint(location, capacity)
		self.water_points[location] = water_point
		return water_point
	
	def total_capacity(self):
		return sum(wp.capacity_liters for wp in self.water_points.values())
	
	def total_current_water(self):
		return sum(wp.current_level for wp in self.water_points.values())
	
	def system_report(self):
		print(f"===== {self.name} Water System Report =====")
		print(f"Number of Water Points: {len(self.water_points)}")
		print(f"Total System Capacity: {self.total_capacity()} liters")
		print(f"Current Water Available: {self.total_current_water():.1f} liters")
		print(f"System Fullness: {(self.total_current_water() / self.total_capacity() * 100):.1f}%")
		print("\nIndividual Water Points:")
		for location, wp in self.water_points.items():
			print(f"\n{location}: {wp.current_level:.1f}/{wp.capacity_liters} liters")


if __name__ == "__main__":
	# Create a neighborhood water system
	kibera_water = NeighborhoodWaterSystem("Kibera")
	
	# Add water points
	kibera_water.add_water_point("Olympic", 5000)
	kibera_water.add_water_point("Gatwekera", 3000)
	kibera_water.add_water_point("Silanga", 4000)
	
	# Simulate some water usage
	olympic_point = kibera_water.water_points["Olympic"]
	olympic_point.dispense_water(1200)  # Dispense 1200 liters
	olympic_point.dispense_water(800)   # Dispense 800 more liters
	
	gatwekera_point = kibera_water.water_points["Gatwekera"]
	gatwekera_point.dispense_water(1500)  # Dispense 1500 liters
	
	# Display system report
	kibera_water.system_report()
	
	# Display detailed report for one water point
	print("\nDetailed Report for Olympic Water Point:")
	olympic_point.status_report()
	
	# Record daily usage and start a new day
	print("\nRecording daily usage...")
	olympic_usage = olympic_point.record_daily_usage()
	print(f"Olympic water point used {olympic_usage} liters today")
	
	# Display updated status after recording
	print("\nUpdated Olympic Water Point Status:")
	olympic_point.status_report()