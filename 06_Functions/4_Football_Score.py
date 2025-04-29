def calculate_team_points(wins, draws, losses):
	"""
	Calculate total points for a football team.
	
	Parameters:
	- wins: Number of matches won
	- draws: Number of matches drawn
	- losses: Number of matches lost
	
	Returns:
	- Total points and total matches played
	"""
	# Points system: 3 points for a win, 1 for a draw, 0 for a loss
	points = (wins * 3) + (draws * 1) + (losses * 0)
	
	# Total matches played
	total_matches = wins + draws + losses
	
	return points, total_matches

# Define another function for win percentage
def calculate_win_percentage(wins, total_matches):
	if total_matches == 0:
		return 0
	else:
		percentage = (wins / total_matches) * 100
		return percentage

# Example usage
if __name__ == "__main__":
	wins = 4
	draws = 2
	losses = 1
	
	# Calculate team points
	team_points, matches_played = calculate_team_points(wins, draws, losses)
	print(f"The SHOFCO team has {team_points} points from {matches_played} matches.")
	
	# Calculate the win percentage
	win_percent = calculate_win_percentage(wins, matches_played)
	print(f"Win percentage: {win_percent:.1f}%")