def calculate_attendance_stats(students, attendance):
	"""Calculate attendance statistics."""
	present_count = 0
	for present in attendance:
		if present:
			present_count += 1
	
	attendance_percentage = (present_count / len(students)) * 100
	
	return {
		"present": present_count,
		"absent": len(students) - present_count,
		"percentage": attendance_percentage
	}

def list_absent_students(students, attendance):
	"""List all absent students."""
	print("\nAbsent students:")
	absent_count = 0
	
	for student in students:
		if student not in attendance:
			print(f"- {student}")
			absent_count += 1
	
	if absent_count == 0:
		print("Everyone is present today!")

if __name__ == "__main__":
	students = ["Wangari", "Otieno", "Akinyi", "Mohammed", "Grace", "Kamau", "Fatuma", "Daniel"]
	attendance = ["Wangari", "Akinyi", "Mohammed", "Kamau", "Fatuma", "Daniel"]
	
	print("SHOFCO School Attendance System")
	print(f"Number of students: {len(students)}")
	
	# Calculate statistics
	stats = calculate_attendance_stats(students, attendance)
	
	# Display attendance summary
	print("\nAttendance Summary:")
	print(f"Present: {stats['present']}")
	print(f"Absent: {stats['absent']}")
	print(f"Attendance rate: {stats['percentage']:.1f}%")
	
	# List absent students
	list_absent_students(students, attendance)