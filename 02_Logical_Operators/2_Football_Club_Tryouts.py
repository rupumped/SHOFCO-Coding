# Player information
plays_school_football = True
recommended_by_coach = False
played_last_season = True
lives_nearby = True

# Different ways to qualify (using OR)
school_path = plays_school_football and recommended_by_coach
previous_player = played_last_season and lives_nearby
special_talent = recommended_by_coach and not played_last_season

# Final eligibility using OR (qualify through any path)
can_tryout = school_path or previous_player or special_talent

# Display results
print("Qualification Paths:")
print("School Path:", school_path)
print("Previous Player Path:", previous_player)
print("Special Talent Path:", special_talent)
print("\nFinal Result - Can Tryout:", can_tryout)

# Experiment: Change the player information variables and see how it affects eligibility