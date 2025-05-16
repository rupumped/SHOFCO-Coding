# Volunteer information
age = 16
has_permission = True
available_saturday = True
available_sunday = False
has_done_training = True
lives_in_community = True

# Check eligibility for different roles
can_help_setup = age >= 14 and available_saturday and lives_in_community
can_help_with_children = age >= 18 and has_done_training and (available_saturday or available_sunday)
can_help_with_food = has_done_training and available_sunday and has_permission
can_volunteer_at_all = can_help_setup or can_help_with_children or can_help_with_food

# Display results
print("Community Event Volunteer Check")
print("----------------------------")
print(f"Age: {age}")
print(f"Has permission: {has_permission}")
print(f"Available Saturday: {available_saturday}")
print(f"Available Sunday: {available_sunday}")
print(f"Completed training: {has_done_training}")
print(f"Lives in community: {lives_in_community}")
print("\nEligible for:")
print(f"Setup team: {can_help_setup}")
print(f"Children's activities: {can_help_with_children}")
print(f"Food distribution: {can_help_with_food}")
print(f"Any volunteer role: {can_volunteer_at_all}")

# Experiment: Change the volunteer information and see how eligibility changes