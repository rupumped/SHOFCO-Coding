def translate_greeting(english_greeting, name):
	"""
	Translates a basic English greeting to Swahili.
	
	Args:
		english_greeting (str): English greeting
		name (str): Name of person being greeted
		
	Returns:
		str: Swahili greeting
	"""
	# Your code here:
	# 1. Create a dictionary of English to Swahili translations
	# 2. Lookup and return the appropriate greeting
	
	# Dictionary of translations
	translations = {
		"hello": "Jambo",
		"good morning": "Habari ya asubuhi",
		"good afternoon": "Habari ya mchana", 
		"good evening": "Habari ya jioni",
		"welcome": "Karibu",
		"how are you": "Habari yako",
		"thank you": "Asante",
		"goodbye": "Kwa heri"
	}
	
	# Convert to lowercase for comparison
	english_lower = english_greeting.lower()
	
	# Find translation
	swahili_greeting = "Jambo"  # Default
	for eng, swa in translations.items():
		if eng in english_lower:
			swahili_greeting = swa
			break
	
	# Format with name
	if name:
		result = f"{swahili_greeting}, {name}!"
	else:
		result = f"{swahili_greeting}!"
	
	return result

if __name__ == "__main__":
	# Test the function
	greeting = input("Enter an English greeting (e.g., 'hello', 'good morning'): ")
	person_name = input("Enter a name (or leave blank): ")
	
	translated = translate_greeting(greeting, person_name)
	print(f"\nTranslation: {translated}")