def count_sms_segments(message):
	"""
	Counts characters in a message and calculates SMS segments.
	
	Args:
		message (str): The SMS message
		
	Returns:
		tuple: (character_count, segment_count, chars_in_last_segment)
	"""
	# Your code here:
	# 1. Count the characters in the message
	# 2. Calculate how many SMS segments needed (160 chars per segment)
	# 3. Calculate remaining characters in the last segment
	
	char_count = len(message)
	
	# Calculate segments (160 chars per segment)
	chars_per_segment = 160
	segment_count = (char_count + chars_per_segment - 1) // chars_per_segment
	
	# Calculate chars in last segment
	if char_count % chars_per_segment == 0:
		chars_in_last = chars_per_segment
	else:
		chars_in_last = char_count % chars_per_segment
	
	return (char_count, segment_count, chars_in_last)

if __name__ == "__main__":
	# Test the function
	message = input("Enter your SMS message: ")
	
	chars, segments, last_segment = count_sms_segments(message)
	
	print(f"Character count: {chars}")
	print(f"SMS segments: {segments}")
	print(f"Characters in last segment: {last_segment}")
	print(f"Cost estimate: {segments * 5} KSh (5 KSh per segment)")