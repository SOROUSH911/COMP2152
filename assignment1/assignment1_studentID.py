'''
Author: <YOUR REAL FIRST AND LAST NAME>
Assignment: #1
'''

# String data type
gym_member = "Alex Alliton"
# Float data type
preferred_weight_kg = 20.5
# Integer data type
highest_reps = 25
# Boolean data type
membership_active = True

# Dictionary containing friend names (strings) mapped to workout minutes (tuples of 3 integers)
workout_stats = {
    "Alex": (30, 45, 20),    # yoga, running, weightlifting
    "Jamie": (45, 30, 35),
    "Taylor": (25, 50, 40)
}

# Calculate and add total workout minutes for each friend
for friend in list(workout_stats.keys()):  # Create a list of keys to avoid dictionary size change during iteration
    total_minutes = sum(workout_stats[friend])
    workout_stats[f"{friend}_Total"] = total_minutes

# List of lists containing workout minutes (2D list/nested list data type)
workout_list = [list(workout_stats[friend]) for friend in ["Alex", "Jamie", "Taylor"]]

# Slice workout_list to get yoga and running minutes for all friends
print("Yoga and running minutes for all friends:")
print([row[0:2] for row in workout_list])

# Slice workout_list to get weightlifting minutes for last two friends
print("\nWeightlifting minutes for last two friends:")
print([row[2] for row in workout_list[1:]])

# Check for friends with total workout minutes >= 120
for friend in ["Alex", "Jamie", "Taylor"]:
    total_minutes = workout_stats[f"{friend}_Total"]
    if total_minutes >= 120:
        print(f"\nGreat job staying active, {friend}!")

# User input and friend lookup
friend_name = input("\nEnter a friend's name to look up their workout stats: ")
if friend_name in workout_stats:
    print(f"\nWorkout stats for {friend_name}:")
    yoga, running, weightlifting = workout_stats[friend_name]
    total = workout_stats[f"{friend_name}_Total"]
    print(f"Yoga: {yoga} minutes")
    print(f"Running: {running} minutes")
    print(f"Weightlifting: {weightlifting} minutes")
    print(f"Total: {total} minutes")
else:
    print(f"\nFriend {friend_name} not found in the records.")

# Find friends with highest and lowest total workout minutes
friends = ["Alex", "Jamie", "Taylor"]
totals = [workout_stats[f"{friend}_Total"] for friend in friends]
max_friend = friends[totals.index(max(totals))]
min_friend = friends[totals.index(min(totals))]

print(f"\nFriend with highest total workout minutes: {max_friend} ({max(totals)} minutes)")
print(f"Friend with lowest total workout minutes: {min_friend} ({min(totals)} minutes)")
