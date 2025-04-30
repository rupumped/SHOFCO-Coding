class Student:
	def __init__(self, name, student_id, grade_level):
		self.name = name
		self.student_id = student_id
		self.grade_level = grade_level
		self.subjects = {}  # Dictionary to store subject: [list of grades]
		self.attendance = {"present": 0, "absent": 0, "late": 0}
	
	def add_grade(self, subject, grade):
		if subject not in self.subjects:
			self.subjects[subject] = []
		self.subjects[subject].append(grade)
	
	def record_attendance(self, status):
		if status in self.attendance:
			self.attendance[status] += 1
	
	def calculate_average(self, subject=None):
		if subject:
			if subject in self.subjects and len(self.subjects[subject]) > 0:
				return sum(self.subjects[subject]) / len(self.subjects[subject])
			return 0
		else:
			all_grades = []
			for grades in self.subjects.values():
				all_grades.extend(grades)
			if len(all_grades) > 0:
				return sum(all_grades) / len(all_grades)
			return 0
	
	def attendance_rate(self):
		total_days = sum(self.attendance.values())
		if total_days == 0:
			return 0
		return (self.attendance["present"] / total_days) * 100
	
	def subject_report(self):
		print(f"Subject Report for {self.name} (ID: {self.student_id})")
		print(f"Grade Level: {self.grade_level}")
		print("-" * 40)
		
		for subject, grades in self.subjects.items():
			avg = self.calculate_average(subject)
			grade_str = ", ".join(str(g) for g in grades)
			print(f"{subject}: {grade_str} (Average: {avg:.1f})")
		
		print("-" * 40)
		print(f"Overall Average: {self.calculate_average():.1f}")
		print(f"Attendance Rate: {self.attendance_rate():.1f}%")
		print(f"Attendance Details: {self.attendance}")


if __name__ == "__main__":
	# Create a student
	student1 = Student("Esther Adhiambo", "SCH2023-042", 8)
	
	# Add grades for different subjects
	student1.add_grade("Mathematics", 85)
	student1.add_grade("Mathematics", 92)
	student1.add_grade("English", 78)
	student1.add_grade("English", 82)
	student1.add_grade("Science", 90)
	student1.add_grade("Social Studies", 88)
	
	# Record attendance
	for _ in range(20):  # 20 present days
		student1.record_attendance("present")
	for _ in range(2):  # 2 absent days
		student1.record_attendance("absent")
	for _ in range(3):  # 3 late days
		student1.record_attendance("late")
	
	# Display student report
	student1.subject_report()