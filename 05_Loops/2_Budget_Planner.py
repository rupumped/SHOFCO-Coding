# Starting values
money = 1000  # shillings
items_bought = 0

print(f"You have {money} KSh to spend.")

while money > 0:
    item_cost = int(input("Enter the cost of the item in KSh (or 0 to stop): "))
    
    # Exit the loop if user enters 0
    if item_cost == 0:
        print("Finished shopping.")
        break
    
    # Check if enough money is available
    if item_cost > money:
        print(f"You don't have enough money. You only have {money} KSh left.")
        continue
    
    # Purchase the item
    money = money - item_cost
    items_bought = items_bought + 1
    print(f"Item purchased! Money remaining: {money} KSh")
    
print(f"Shopping summary: Bought {items_bought} items and have {money} KSh left.")