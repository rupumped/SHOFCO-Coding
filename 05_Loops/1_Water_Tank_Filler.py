# Starting values
tank_capacity = 100  # liters
current_level = 0
bucket_size = 10  # liters

print("Starting to fill the water tank...")

# Keep adding water until tank is full or almost full
while current_level < tank_capacity:
    current_level = current_level + bucket_size
    
    # Don't overflow the tank
    if current_level > tank_capacity:
        current_level = tank_capacity
        
    print(f"Added water. Tank level: {current_level}/{tank_capacity} liters")
    
print("The water tank is now full!")