def analyze_transaction(transaction_type, amount):
	"""
	Analyze a mobile money transaction and give advice.
	
	Parameters:
	- transaction_type: 'send', 'receive', or 'withdraw'
	- amount: Amount in Kenyan Shillings
	
	Returns:
	- Transaction details and advice
	"""
	# Calculate fees based on transaction type
	if transaction_type == "send":
		if amount <= 100:
			fee = 0
		elif amount <= 500:
			fee = 11
		elif amount <= 1000:
			fee = 15
		else:
			fee = 25
		
		advice = "Remember to confirm the recipient's number before sending."
		
	elif transaction_type == "withdraw":
		if amount <= 100:
			fee = 10
		elif amount <= 500:
			fee = 27
		elif amount <= 1000:
			fee = 28
		else:
			fee = 33
		
		advice = "Always count your money before leaving the agent."
		
	elif transaction_type == "receive":
		fee = 0
		advice = "Check that the amount received matches what you expected."
		
	else:
		print("Unknown transaction type")
		return {}
	
	total_cost = amount + fee
	
	return {
		"Transaction": transaction_type,
		"Amount": amount,
		"Fee": fee,
		"Total": total_cost,
		"Advice": advice
	}

# Example usage
if __name__ == "__main__":
	result = analyze_transaction("send", 500)
	print("Transaction Details:")
	for key, value in result.items():
		print(f"{key}: {value}")