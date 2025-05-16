def collect_responses(question, num_respondents):
	"""Collect responses for a single survey question."""
	responses = []
	
	print(f"\nQuestion: {question}")
	
	# Collect responses from the specified number of community members
	for person in range(1, num_respondents + 1):
		while True:
			try:
				score = int(input(f"Person {person}'s response: "))
				if 1 <= score <= 5:
					responses.append(score)
					break
				else:
					print("Please enter a number between 1 and 5.")
			except ValueError:
				print("Please enter a valid number.")
	
	return responses

def analyze_question(question, responses):
	"""Analyze responses for a single question."""
	average = sum(responses) / len(responses)
	
	# Show responses for this question
	print(f"Responses: {responses}")
	print(f"Average score: {average:.1f}/5")
	
	return average

def extract_category(question):
	"""Extract category name from question text."""
	return question.split("?")[0].replace("How satisfied are you with ", "")

def display_survey_results(questions, category_scores):
	"""Display overall survey results."""
	print("\nOverall Survey Results:")
	for i in range(len(questions)):
		category = extract_category(questions[i])
		print(f"{category}: {category_scores[i]:.1f}/5")
	
	# Find highest and lowest rated categories
	highest_index = category_scores.index(max(category_scores))
	lowest_index = category_scores.index(min(category_scores))
	
	highest_category = extract_category(questions[highest_index])
	lowest_category = extract_category(questions[lowest_index])
	
	print(f"\nHighest rated: {highest_category} ({category_scores[highest_index]:.1f}/5)")
	print(f"Lowest rated: {lowest_category} ({category_scores[lowest_index]:.1f}/5)")

if __name__ == "__main__":
	# Survey questions
	questions = [
		"How satisfied are you with water access? (1-5)",
		"How satisfied are you with educational programs? (1-5)",
		"How satisfied are you with health services? (1-5)",
		"How satisfied are you with community safety? (1-5)"
	]
	
	# Number of people to survey per question
	num_respondents = 3  # Can be changed for a real survey
	
	# List to store average scores
	category_scores = []
	
	print("SHOFCO Community Survey Analysis")
	print("--------------------------------")
	
	# Process each question
	for question in questions:
		responses = collect_responses(question, num_respondents)
		average = analyze_question(question, responses)
		category_scores.append(average)
	
	# Display overall results
	display_survey_results(questions, category_scores)