import nbformat as nbf

nb = nbf.v4.new_notebook()

# Create cells
cells = [
    nbf.v4.new_markdown_cell('''# Assignment 1

'''
'''
Author: <YOUR REAL FIRST AND LAST NAME>
Assignment: #1
'''
),
    
    nbf.v4.new_code_cell('''gym_member = "Alex Alliton"           # str
preferred_weight_kg = 20.5         # float
highest_reps = 25                  # int
membership_active = True           # bool'''),
    
    nbf.v4.new_code_cell('''# Dictionary data type: dict containing str keys and tuple values (str: tuple[int, int, int])
workout_stats = {
    "Alex": (30, 45, 20),    # yoga, running, weightlifting
    "Jamie": (45, 30, 35),
    "Taylor": (25, 50, 40)
}'''),
    
    nbf.v4.new_code_cell('''# Calculate and add total workout minutes for each friend
for friend in list(workout_stats.keys()):
    total_minutes = sum(workout_stats[friend])
    workout_stats[f"{friend}_Total"] = total_minutes

# Display the updated dictionary with totals
for friend in ["Alex", "Jamie", "Taylor"]:
    print(f"{friend}'s total workout minutes: {workout_stats[f'{friend}_Total']}")'''),
    
    nbf.v4.new_code_cell('''# 2D list data type: list[list[int]] - A list of lists where each inner list contains 3 integers
workout_list = [list(workout_stats[friend]) for friend in ["Alex", "Jamie", "Taylor"]]

print("Workout list (rows=friends, columns=activities):")
for friend, minutes in zip(["Alex", "Jamie", "Taylor"], workout_list):
    print(f"{friend}: {minutes}")'''),
    
    nbf.v4.new_code_cell('''# Extract and print yoga and running minutes for all friends
print("Yoga and running minutes for all friends:")
yoga_running = [row[0:2] for row in workout_list]
for friend, minutes in zip(["Alex", "Jamie", "Taylor"], yoga_running):
    print(f"{friend}: {minutes}")

# Extract and print weightlifting minutes for last two friends
print("\nWeightlifting minutes for last two friends:")
weightlifting = [row[2] for row in workout_list[1:]]
for friend, minutes in zip(["Jamie", "Taylor"], weightlifting):
    print(f"{friend}: {minutes}")'''),
    
    nbf.v4.new_code_cell('''# Check for friends with total workout minutes >= 120
for friend in ["Alex", "Jamie", "Taylor"]:
    total_minutes = workout_stats[f"{friend}_Total"]
    if total_minutes >= 120:
        print(f"Great job staying active, {friend}!")'''),
    
    nbf.v4.new_code_cell('''# User input and friend lookup functionality
friend_name = input("Enter a friend's name to look up their workout stats: ")
if friend_name in workout_stats:
    print(f"\nWorkout stats for {friend_name}:")
    yoga, running, weightlifting = workout_stats[friend_name]
    total = workout_stats[f"{friend_name}_Total"]
    print(f"Yoga: {yoga} minutes")
    print(f"Running: {running} minutes")
    print(f"Weightlifting: {weightlifting} minutes")
    print(f"Total: {total} minutes")
else:
    print(f"Friend {friend_name} not found in the records.")'''),
    
    nbf.v4.new_code_cell('''# Find and display friends with highest and lowest total workout minutes
friends = ["Alex", "Jamie", "Taylor"]
totals = [workout_stats[f"{friend}_Total"] for friend in friends]

max_friend = friends[totals.index(max(totals))]
min_friend = friends[totals.index(min(totals))]

print(f"Friend with highest total workout minutes: {max_friend} ({max(totals)} minutes)")
print(f"Friend with lowest total workout minutes: {min_friend} ({min(totals)} minutes)")''')
]

nb['cells'] = cells

# Write the notebook to a file
with open('assignment1_studentID.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
