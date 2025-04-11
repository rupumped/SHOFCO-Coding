# Household situations
has_small_children = True
has_elderly_people = False
water_outage_days = 3
is_community_volunteer = True

# Calculate priority factors
is_vulnerable_household = has_small_children or has_elderly_people
has_long_outage = water_outage_days >= 2
is_priority_member = is_community_volunteer and has_long_outage

# Determine access priority
qualifies_for_emergency_access = is_vulnerable_household and has_long_outage
qualifies_for_priority_access = is_priority_member or (is_vulnerable_household and not has_long_outage)

if qualifies_for_emergency_access:
    print("Household qualifies for emergency access. Let them get water now.")
elif qualifies_for_priority_access:
    print("Household qualifies for priority access. If there are no emergency access customers waiting, allow this household to cut the line.")
else:
    print("Household has regular access to water.")

# Challenge: Change the household situations and see how the access changes