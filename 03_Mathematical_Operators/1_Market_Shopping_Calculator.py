# Item prices in Kenyan Shillings
tomatoes_price = int(input("Price per Tomato: "))  # per tomato
onions_price = int(input("Price per Onion: "))    # per onion
maize_flour_price = int(input("Price per kg Maize Flour: "))  # per kg
beans_price = int(input("Price per kg Beans: "))    # per kg

# Quantities
tomatoes_qty = int(input("Number of Tomatoes: "))
onions_qty = int(input("Number of Onions: "))
maize_flour_qty = float(input("Kilos of Maize Flour: "))
beans_qty = float(input("Kilos of Beans: "))

# Calculate costs for each item
tomatoes_cost = tomatoes_price * tomatoes_qty
onions_cost = onions_price * onions_qty
maize_flour_cost = maize_flour_price * maize_flour_qty
beans_cost = beans_price * beans_qty

# Calculate total cost
total_cost = tomatoes_cost + onions_cost + maize_flour_cost + beans_cost

# Calculate change from 1000 KSh
money_given = int(input("Money Given: "))
change = money_given - total_cost

# Display the shopping receipt
print("===== Market Receipt =====")
print(f"{tomatoes_qty} Tomatoes: {tomatoes_cost} KSh")
print(f"{onions_qty} Onions: {onions_cost} KSh")
print(f"{maize_flour_qty} kg Maize Flour: {maize_flour_cost} KSh")
print(f"{beans_qty} kg Beans: {beans_cost} KSh")
print("-------------------------")
print(f"Total: {total_cost} KSh")
print(f"Paid: {money_given} KSh")
print(f"Change: {change} KSh")
print("=========================")