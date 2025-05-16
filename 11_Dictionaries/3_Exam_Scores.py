def display_student_scores(names, math_scores, english_scores, average_scores):
	"""Display all student scores in a formatted table."""
	print("SHOFCO School Exam Results")
	print("-------------------------")
	print("Name\t\tMath\tEnglish\tAverage")
	print("----\t\t----\t-------\t-------")
	
	for i in range(len(names)):
		# Ensure proper spacing in the table
		name_spacing = "\t" if len(names[i]) >= 8 else "\t\t"
		print(f"{names[i]}{name_spacing}{math_scores[i]}\t{english_scores[i]}\t{average_scores[i]:.1f}")

def calculate_average_scores(math_scores, english_scores):
	"""Calculate the average score for each student."""
	average_scores = []
	
	for i in range(len(math_scores)):
		student_average = (math_scores[i] + english_scores[i]) / 2
		average_scores.append(student_average)
	
	return average_scores

def calculate_class_averages(math_scores, english_scores, average_scores):
	"""Calculate class-wide average scores."""
	math_average = sum(math_scores) / len(math_scores)
	english_average = sum(english_scores) / len(english_scores)
	overall_average = sum(average_scores) / len(average_scores)
	
	return {
		"math": math_average,
		"english": english_average,
		"overall": overall_average
	}

def find_top_students(names, math_scores, english_scores, average_scores):
	"""Find the top-performing students in each category."""
	top_math_index = math_scores.index(max(math_scores))
	top_english_index = english_scores.index(max(english_scores))
	top_overall_index = average_scores.index(max(average_scores))
	
	return {
		"math": {"name": names[top_math_index], "score": math_scores[top_math_index]},
		"english": {"name": names[top_english_index], "score": english_scores[top_english_index]},
		"overall": {"name": names[top_overall_index], "score": average_scores[top_overall_index]}
	}

def identify_struggling_students(names, math_scores, english_scores, passing_grade=70):
	"""Identify students who are below the passing grade."""
	struggling_students = []
	
	for i in range(len(names)):
		if math_scores[i] < passing_grade:
			struggling_students.append({
				"name": names[i],
				"subject": "Math",
				"score": math_scores[i]
			})
		
		if english_scores[i] < passing_grade:
			struggling_students.append({
				"name": names[i],
				"subject": "English",
				"score": english_scores[i]
			})
	
	return struggling_students

if __name__ == "__main__":
	# Student names and scores
	names = ["Wangari", "Otieno", "Akinyi", "Mohammed", "Grace", "Kamau", "Fatuma", "Daniel"]
	math_scores = [78, 85, 92, 65, 88, 72, 95, 81]
	english_scores = [82, 78, 90, 75, 85, 68, 88, 79]
	
	# Calculate average scores for each student
	average_scores = calculate_average_scores(math_scores, english_scores)
	
	# Display all student scores
	display_student_scores(names, math_scores, english_scores, average_scores)
	
	# Calculate and display class averages
	class_averages = calculate_class_averages(math_scores, english_scores, average_scores)
	
	print("\nClass Averages:")
	print(f"Math: {class_averages['math']:.1f}")
	print(f"English: {class_averages['english']:.1f}")
	print(f"Overall: {class_averages['overall']:.1f}")
	
	# Find and display top students
	top_students = find_top_students(names, math_scores, english_scores, average_scores)
	
	print("\nTop Students:")
	print(f"Math: {top_students['math']['name']} ({top_students['math']['score']})")
	print(f"English: {top_students['english']['name']} ({top_students['english']['score']})")
	print(f"Overall: {top_students['overall']['name']} ({top_students['overall']['score']:.1f})")
	
	# Identify and display struggling students
	struggling_students = identify_struggling_students(names, math_scores, english_scores)
	
	print("\nStudents Needing Extra Help:")
	if struggling_students:
		for student in struggling_students:
			print(f"{student['name']} needs help in {student['subject']}: {student['score']}")
	else:
		print("All students are performing above the passing grade!")