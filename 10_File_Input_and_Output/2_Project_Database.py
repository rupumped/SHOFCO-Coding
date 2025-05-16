def add_project(student_name, project_title, description, date_completed):
	"""
	Adds a new student project to the projects database.
	
	Args:
		student_name (str): Name of the student
		project_title (str): Title of the project
		description (str): Description of the project
		date_completed (str): Date the project was completed
	"""
	# Create a unique filename for the project
	safe_title = project_title.replace(" ", "_").lower()
	filename = f"{safe_title}_{student_name.replace(' ', '_').lower()}.txt"
	
	# Save detailed project info to individual file
	with open(f"projects/{filename}", "w") as project_file:
		project_file.write(f"Project: {project_title}\n")
		project_file.write(f"Student: {student_name}\n")
		project_file.write(f"Date Completed: {date_completed}\n")
		project_file.write(f"Description:\n{description}\n")
	
	# Add to project index file
	with open("projects/index.txt", "a") as index_file:
		index_file.write(f"{student_name},{project_title},{date_completed},{filename}\n")
	
	print(f"Project '{project_title}' has been added to the database.")

def list_student_projects(student_name):
	"""
	Lists all projects by a specific student.
	
	Args:
		student_name (str): Name of the student
	
	Returns:
		list: List of the student's projects
	"""
	projects = []
	try:
		with open("projects/index.txt", "r") as file:
			for line in file:
				parts = line.strip().split(",")
				if len(parts) >= 4 and parts[0].lower() == student_name.lower():
					projects.append((parts[1], parts[2], parts[3]))
		return projects
	except FileNotFoundError:
		print("No projects database found.")
		return []

def display_project_details(filename):
	"""
	Displays the complete details of a specific project.
	
	Args:
		filename (str): Filename of the project
	"""
	try:
		with open(f"projects/{filename}", "r") as file:
			content = file.read()
			print("\n" + "=" * 50)
			print(content)
			print("=" * 50)
	except FileNotFoundError:
		print(f"Project file '{filename}' not found.")

def search_projects(keyword):
	"""
	Searches all projects for a specific keyword.
	
	Args:
		keyword (str): Keyword to search for
	
	Returns:
		list: List of matching projects
	"""
	matches = []
	
	# First search in index
	try:
		with open("projects/index.txt", "r") as index_file:
			for line in index_file:
				if keyword.lower() in line.lower():
					parts = line.strip().split(",")
					if len(parts) >= 4:
						matches.append((parts[0], parts[1], parts[2], parts[3]))
	except FileNotFoundError:
		print("No projects database found.")
	
	# Then search in individual project files
	try:
		with open("projects/index.txt", "r") as index_file:
			for line in index_file:
				parts = line.strip().split(",")
				if len(parts) >= 4:
					project_filename = parts[3]
					try:
						with open(f"projects/{project_filename}", "r") as project_file:
							content = project_file.read()
							if keyword.lower() in content.lower() and (parts[0], parts[1], parts[2], parts[3]) not in matches:
								matches.append((parts[0], parts[1], parts[2], parts[3]))
					except FileNotFoundError:
						pass
	except FileNotFoundError:
		pass
					
	return matches

def ensure_project_directory():
	"""
	Makes sure the projects directory exists.
	"""
	import os
	if not os.path.exists("projects"):
		os.makedirs("projects")
		# Create empty index file
		with open("projects/index.txt", "w") as f:
			pass
		print("Created projects directory.")

if __name__ == "__main__":
	print("SHOFCO Student Projects Database")
	print("-----------------------------")
	
	# Make sure the projects directory exists
	ensure_project_directory()
	
	while True:
		print("\nOptions:")
		print("1. Add new project")
		print("2. List student's projects")
		print("3. View project details")
		print("4. Search projects")
		print("5. Exit")
		
		choice = input("\nEnter your choice (1-5): ")
		
		if choice == "1":
			student = input("Student name: ")
			title = input("Project title: ")
			date = input("Date completed (DD/MM/YYYY): ")
			print("Project description (type 'done' on a new line when finished):")
			
			lines = []
			while True:
				line = input()
				if line.lower() == "done":
					break
				lines.append(line)
			
			description = "\n".join(lines)
			add_project(student, title, description, date)
			
		elif choice == "2":
			student = input("Enter student name: ")
			projects = list_student_projects(student)
			
			if projects:
				print(f"\n{student}'s Projects:")
				for i, (title, date, filename) in enumerate(projects, 1):
					print(f"{i}. {title} (completed: {date})")
			else:
				print(f"No projects found for {student}.")
				
		elif choice == "3":
			student = input("Enter student name: ")
			projects = list_student_projects(student)
			
			if projects:
				print(f"\n{student}'s Projects:")
				for i, (title, date, filename) in enumerate(projects, 1):
					print(f"{i}. {title} (completed: {date})")
				
				choice = input("\nEnter number to view details: ")
				try:
					index = int(choice) - 1
					if 0 <= index < len(projects):
						display_project_details(projects[index][2])
					else:
						print("Invalid project number.")
				except ValueError:
					print("Please enter a number.")
			else:
				print(f"No projects found for {student}.")
				
		elif choice == "4":
			keyword = input("Enter search term: ")
			matches = search_projects(keyword)
			
			if matches:
				print(f"\nFound {len(matches)} matching projects:")
				for i, (student, title, date, _) in enumerate(matches, 1):
					print(f"{i}. {title} by {student} (completed: {date})")
					
				view = input("\nEnter number to view details (or 0 to skip): ")
				try:
					index = int(view) - 1
					if 0 <= index < len(matches):
						display_project_details(matches[index][3])
				except ValueError:
					pass
			else:
				print(f"No projects matching '{keyword}' found.")
				
		elif choice == "5":
			print("Thank you for using the Projects Database!")
			break
			
		else:
			print("Invalid choice. Please try again.")