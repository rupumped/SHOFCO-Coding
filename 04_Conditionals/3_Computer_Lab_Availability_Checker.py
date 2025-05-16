# Current conditions
is_school_day = True
is_holiday = False
current_hour = 14  # 24-hour format (2 PM)
is_special_event = False
is_maintenance_day = False

# Check time-based availability
during_school_hours = current_hour >= 8 and current_hour < 16
after_school_hours = current_hour >= 16 and current_hour < 18

# Check day-based availability
open_for_regular_use = is_school_day and not is_holiday and not is_special_event and not is_maintenance_day
open_for_after_school = is_school_day and not is_holiday and after_school_hours and not is_maintenance_day
open_for_weekend = not is_school_day and not is_holiday and current_hour >= 10 and current_hour < 15 and not is_maintenance_day

# Final availability 
lab_is_available = (open_for_regular_use and during_school_hours) or open_for_after_school or open_for_weekend

# Display results
print("Computer Lab Availability Check")
print("------------------------------")
print("Current hour:", current_hour)
print("School day:", is_school_day)
print("Holiday:", is_holiday)
print("Special event:", is_special_event)
print("Maintenance day:", is_maintenance_day)

if lab_is_available:
    print("The lab is available for use. Come on in!")
else:
    print("Sorry. The lab is not available currently. Please try again later.")

# Try changing the current conditions to see how availability changes