# Test scores (out of 100)
math_score = int(input("Math Score: "))
english_score = int(input("English Score: "))
science_score = int(input("Science Score: "))
history_score = int(input("History Score: "))
computer_score = int(input("Computer Score: "))

# Calculate the sum of all scores
total_score = math_score + english_score + science_score + history_score + computer_score

# Calculate the average score
number_of_subjects = 5
average_score = total_score / number_of_subjects

# Calculate percentage of maximum possible points
maximum_possible = number_of_subjects * 100
percentage = (total_score / maximum_possible) * 100

# Points needed for next grade level (if B is 80-89% and A is 90-100%)
points_for_A_grade = (90 * maximum_possible / 100) - total_score

# Display results
print("===== Grade Calculator =====")
print(f"Math: {math_score}/100")
print(f"English: {english_score}/100")
print(f"Science: {science_score}/100")
print(f"History: {history_score}/100")
print(f"Computer: {computer_score}/100")
print("---------------------------")
print(f"Total Score: {total_score}/{maximum_possible}")
print(f"Average Score: {average_score:.2f}/100")
print(f"Percentage: {percentage:.2f}%")
print(f"Points needed for A grade: {points_for_A_grade}")
print("===========================")