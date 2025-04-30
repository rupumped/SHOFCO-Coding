import csv
import os
from datetime import datetime

def save_survey_response(name, age, service_used, rating, feedback):
	"""
	Saves a survey response to a CSV file.
	
	Args:
		name (str): Name of respondent
		age (int): Age of respondent
		service_used (str): SHOFCO service being rated
		rating (int): Rating from 1-5
		feedback (str): Written feedback
	"""
	# Check if file exists, if not create with headers
	file_exists = os.path.isfile("survey_responses.csv")
	
	with open("survey_responses.csv", "a", newline='') as csvfile:
		fieldnames = ["name", "age", "service", "rating", "feedback", "date"]
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		
		# Write headers if file is being created for the first time
		if not file_exists:
			writer.writeheader()
		
		# Add the new survey response
		writer.writerow({
			"name": name,
			"age": age,
			"service": service_used,
			"rating": rating,
			"feedback": feedback,
			"date": datetime.now().strftime("%d/%m/%Y")
		})
		
	print("Thank you! Your survey response has been recorded.")

def analyze_service_ratings(service_name):
	"""
	Analyzes ratings for a specific service and saves summary to a CSV file.
	
	Args:
		service_name (str): Name of service to analyze
	
	Returns:
		float: Average rating for the service
	"""
	try:
		total_rating = 0
		count = 0
		feedback_list = []
		age_groups = {"under_18": 0, "18_to_30": 0, "over_30": 0}
		
		# Read all responses
		with open("survey_responses.csv", "r", newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			
			for row in reader:
				if row["service"].lower() == service_name.lower():
					# Add rating to total
					total_rating += int(row["rating"])
					count += 1
					
					# Collect feedback
					feedback_list.append(row["feedback"])
					
					# Count age groups
					age = int(row["age"])
					if age < 18:
						age_groups["under_18"] += 1
					elif age <= 30:
						age_groups["18_to_30"] += 1
					else:
						age_groups["over_30"] += 1
		
		# Calculate average
		if count > 0:
			average_rating = total_rating / count
			
			# Save analysis to a CSV file
			analysis_filename = f"{service_name.replace(' ', '_').lower()}_analysis.csv"
			
			with open(analysis_filename, "w", newline='') as csvfile:
				writer = csv.writer(csvfile)
				writer.writerow(["Analysis Metric", "Value"])
				writer.writerow(["Service", service_name])
				writer.writerow(["Number of responses", count])
				writer.writerow(["Average rating", f"{average_rating:.1f}/5"])
				writer.writerow(["Respondents under 18", age_groups["under_18"]])
				writer.writerow(["Respondents 18-30", age_groups["18_to_30"]])
				writer.writerow(["Respondents over 30", age_groups["over_30"]])
				writer.writerow([])
				writer.writerow(["Feedback Comments"])
				
				for feedback in feedback_list:
					writer.writerow([feedback])
			
			return average_rating
		else:
			print(f"No ratings found for {service_name}")
			return 0
			
	except FileNotFoundError:
		print("No survey responses have been recorded yet.")
		return 0

def display_all_services():
	"""
	Reads the survey CSV file and displays all unique services mentioned.
	"""
	try:
		services = set()
		with open("survey_responses.csv", "r", newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			
			for row in reader:
				services.add(row["service"])
		
		if services:
			print("\nServices mentioned in surveys:")
			for service in sorted(services):
				print(f"- {service}")
		else:
			print("No services found in survey data.")
	except FileNotFoundError:
		print("No survey responses have been recorded yet.")

def generate_service_summary_report():
	"""
	Creates a summary report of all services and their average ratings.
	"""
	try:
		# Dictionary to store service ratings
		service_data = {}
		
		with open("survey_responses.csv", "r", newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			
			for row in reader:
				service = row["service"]
				rating = int(row["rating"])
				
				if service in service_data:
					service_data[service]["total"] += rating
					service_data[service]["count"] += 1
				else:
					service_data[service] = {"total": rating, "count": 1}
		
		# Create the summary report
		with open("service_summary_report.csv", "w", newline='') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow(["Service", "Number of Responses", "Average Rating"])
			
			for service, data in sorted(service_data.items()):
				avg = data["total"] / data["count"]
				writer.writerow([service, data["count"], f"{avg:.1f}"])
		
		print("Service summary report generated successfully.")
		print("Saved to 'service_summary_report.csv'")
		
	except FileNotFoundError:
		print("No survey responses have been recorded yet.")

if __name__ == "__main__":
	print("SHOFCO Community Survey Tool")
	print("--------------------------")
	
	while True:
		print("\nMenu:")
		print("1. Submit a new survey response")
		print("2. Analyze ratings for a service")
		print("3. View all services")
		print("4. Generate service summary report")
		print("5. Exit")
		
		choice = input("\nEnter your choice (1-5): ")
		
		if choice == "1":
			name = input("Your name: ")
			age = input("Your age: ")
			service = input("Which SHOFCO service are you rating? ")
			rating = input("Rating (1-5): ")
			feedback = input("Please share your feedback: ")
			save_survey_response(name, age, service, rating, feedback)
			
		elif choice == "2":
			service = input("Enter the service name to analyze: ")
			avg = analyze_service_ratings(service)
			if avg > 0:
				print(f"The average rating for {service} is {avg:.1f}/5")
				print(f"Full analysis saved to {service.replace(' ', '_').lower()}_analysis.csv")
				
		elif choice == "3":
			display_all_services()
			
		elif choice == "4":
			generate_service_summary_report()
			
		elif choice == "5":
			print("Thank you for using the SHOFCO Survey Tool!")
			break
			
		else:
			print("Invalid choice. Please try again.")