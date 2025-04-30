def trace_water_flow(network, current_point, water_remaining, path=None, all_paths=None):
	"""
	Recursively trace water flow through the SHOFCO water distribution network
	
	Args:
		network: Dictionary representing the water network connections
		current_point: Current water point in the network
		water_remaining: Amount of water remaining to distribute (liters)
		path: Current path being traced
		all_paths: All valid paths found
	
	Returns:
		List of all valid distribution paths
	"""
	# Initialize tracking variables
	if path is None:
		path = [current_point]
	if all_paths is None:
		all_paths = []
	
	# Base case: if there's no water left or we've reached a delivery point
	if water_remaining <= 0:
		return all_paths
	
	if current_point.startswith("D"):  # Delivery point reached
		print(f"Water delivered: {path} with {water_remaining} liters remaining")
		all_paths.append(path.copy())
		return all_paths
	
	# Get all connected points in the water network
	connections = network.get(current_point, [])
	
	# For each connection, recursively trace the water flow
	for connection, pipe_capacity in connections:
		# Skip if we've already visited this connection
		if connection in path:
			continue
		
		# Calculate water that can flow through this pipe
		flow_amount = min(water_remaining, pipe_capacity)
		
		if flow_amount > 0:
			# Add connection to current path
			path.append(connection)
			
			# Display current flow state
			print(f"Flowing {flow_amount} liters from {current_point} to {connection}")
			
			# Recursively trace flow to this connection
			trace_water_flow(network, connection, flow_amount, path, all_paths)
			
			# Backtrack to try other paths
			path.pop()
	
	return all_paths


if __name__ == "__main__":
	print("SHOFCO Water Distribution Network Simulator")
	print("This program models how water flows through Kibera's distribution system\n")
	
	# Create a model of the SHOFCO water distribution network
	# T = Tank, J = Junction, D = Delivery Point
	# (connection, pipe capacity in liters)
	water_network = {
		"T1": [("J1", 5000), ("J2", 3000)],           # Main tank connects to two junctions
		"J1": [("J3", 2000), ("D1", 1000)],           # Junction 1 connects to another junction and a delivery point
		"J2": [("J4", 2000), ("D2", 1000)],           # Junction 2 connects to another junction and a delivery point
		"J3": [("D3", 1500), ("D4", 500)],            # Junction 3 connects to two delivery points
		"J4": [("D5", 1000), ("D6", 1000)]            # Junction 4 connects to two delivery points
	}
	
	# Starting conditions
	main_tank = "T1"
	initial_water = int(input("Enter water amount in main tank (liters): "))
	
	print(f"\nTracing water flow from main tank {main_tank} with {initial_water} liters\n")
	distribution_paths = trace_water_flow(water_network, main_tank, initial_water)
	
	print(f"\nFound {len(distribution_paths)} possible water distribution paths")
	
	# Calculate total delivery points served
	delivery_points = set()
	for path in distribution_paths:
		for point in path:
			if point.startswith("D"):
				delivery_points.add(point)
	
	print(f"This distribution can serve {len(delivery_points)} delivery points: {', '.join(sorted(delivery_points))}")