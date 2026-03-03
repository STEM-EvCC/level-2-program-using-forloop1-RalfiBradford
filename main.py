# List of mission data
mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

# Variables to keep track of counts
total_missions = 0
successful_missions = 0

# list to store missions before the year 2000
missions_before_2000 = []

# For loop to go through each mission
for i in range(len(mission_names)):
    
    # Count total missions
    total_missions += 1
    
    # Count successful missions
    if mission_success[i] == True:
        successful_missions += 1
    
    # Check if mission was launched before 2000
    if mission_years[i] < 2000:
        missions_before_2000.append(mission_names[i])

# Calculate success rate
success_rate = (successful_missions / total_missions) * 100

# Print the results per format
print("Total number of missions:", total_missions)
print("Number of successful missions:", successful_missions)
print("Success rate: {:.2f}%".format(success_rate))
print("Missions launched before the year 2000:")

# Print each mission on its own line with a dash
for mission in missions_before_2000:
    print("-", mission)