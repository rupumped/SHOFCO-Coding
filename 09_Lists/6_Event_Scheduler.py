def display_events(names, days, times, locations):
	"""Display a nicely formatted event schedule."""
	print("\nSHOFCO Weekly Community Events:")
	print("-------------------------------")
	print("Event\t\t\tDay\t\tTime\t\tLocation")
	print("-----\t\t\t---\t\t----\t\t--------")
	
	for i in range(len(names)):
		# Adjust spacing based on text length
		name_space = "\t\t" if len(names[i]) < 16 else "\t"
		day_space = "\t\t" if len(days[i]) < 8 else "\t"
		time_space = "\t\t" if len(times[i]) < 8 else "\t"
		
		print(f"{names[i]}{name_space}{days[i]}{day_space}{times[i]}{time_space}{locations[i]}")

def search_by_day(event_names, event_days, event_times, event_locations, search_day):
	"""Search for events on a specific day."""
	print(f"\nEvents on {search_day}:")
	found = False
	
	for i in range(len(event_days)):
		if event_days[i] == search_day:
			print(f"- {event_names[i]} at {event_times[i]}, {event_locations[i]}")
			found = True
	
	if not found:
		print(f"No events found on {search_day}")

def search_by_location(event_names, event_days, event_times, event_locations, search_location):
	"""Search for events at a specific location."""
	print(f"\nEvents at {search_location}:")
	found = False
	
	for i in range(len(event_locations)):
		if search_location.lower() in event_locations[i].lower():
			print(f"- {event_names[i]} on {event_days[i]} at {event_times[i]}")
			found = True
	
	if not found:
		print(f"No events found at {search_location}")

def add_new_event(event_names, event_days, event_times, event_locations):
	"""Add a new event to the schedule."""
	new_name = input("Enter event name: ")
	new_day = input("Enter event day: ")
	new_time = input("Enter event time: ")
	new_location = input("Enter event location: ")
	
	# Add the new event to our lists
	event_names.append(new_name)
	event_days.append(new_day)
	event_times.append(new_time)
	event_locations.append(new_location)
	
	print(f"Event '{new_name}' added successfully!")

def event_scheduler_menu(event_names, event_days, event_times, event_locations):
	"""Display and handle the event scheduler menu."""
	while True:
		print("\nOptions:")
		print("1. Search for events by day")
		print("2. Search for events by location")
		print("3. Add new event")
		print("4. Display all events")
		print("5. Exit")
		
		choice = input("Enter your choice (1-5): ")
		
		if choice == "1":
			day_search = input("Enter day to search for: ").capitalize()
			search_by_day(event_names, event_days, event_times, event_locations, day_search)
		
		elif choice == "2":
			location_search = input("Enter location to search for: ")
			search_by_location(event_names, event_days, event_times, event_locations, location_search)
		
		elif choice == "3":
			add_new_event(event_names, event_days, event_times, event_locations)
			display_events(event_names, event_days, event_times, event_locations)
		
		elif choice == "4":
			display_events(event_names, event_days, event_times, event_locations)
		
		elif choice == "5":
			print("Thank you for using the SHOFCO Event Scheduler!")
			break
		
		else:
			print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
	# Lists to store event information
	event_names = ["Computer Class", "Health Workshop", "Community Meeting", "Sports Day", "Library Hour"]
	event_days = ["Monday", "Wednesday", "Thursday", "Saturday", "Friday"]
	event_times = ["3:00 PM", "10:00 AM", "5:30 PM", "9:00 AM", "2:00 PM"]
	event_locations = ["Computer Lab", "Health Center", "Community Hall", "Sports Field", "Library"]
	
	print("SHOFCO Community Event Scheduler")
	print("===============================")
	
	# Display the initial schedule
	display_events(event_names, event_days, event_times, event_locations)
	
	# Show the menu
	event_scheduler_menu(event_names, event_days, event_times, event_locations)