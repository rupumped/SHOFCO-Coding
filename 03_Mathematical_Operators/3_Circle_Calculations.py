import math

# Circle calculations
radius = float(input("Radius (m): "))  # meters
area_circle = math.pi * radius ** 2  # square meters
circumference = 2 * math.pi * radius   # meters

# Display results
print("===== Circle Calculations =====")
print("Circle:")
print(f"Radius: {radius} m")
print(f"Area: {area_circle:.2f} square meters")
print(f"Circumference: {circumference:.2f} meters")
print("================================")

# Try creating your own geometric calculations for other shapes!