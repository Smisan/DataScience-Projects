'''

Radiation Measurement Analysis Program :
Dr. Eleanor, a renowned physicist, is conducting an experiment to measure 
the average radiation levels in various environments with high amounts of radioactive waste. 
This program is designed to efficiently handle radiation measurements collected by Dr. Eleanor for her experiment. 
It allows Dr. Eleanor to input radiation measurements for each location and calculate essential statistical
insights to analyze the data.
The program utilizes loops effectively to handle the repetitive nature of data input and calculations. 
It uses a for loop to iterate over each location's dataset and nested loops to process individual measurements within those sets.
Dr. Eleanor can continue inputting data until she decides to stop, utilizing a while loop to facilitate continuous data entry.

'''

import numpy as np
#Define a dictionary to store locations and their radiation levels
locations = {'City Centre':[22,19,20,31,28], 'Industrial Zone': [35,32,30,37,40],
             'Residential District': [15,12,18,20,14], 'Rural Outskirts': [9,13,16,14,7],
             'Downtown': [25,18,22,21,26]}

#Define a function to calculate average radiation levels
def calculate_average(levels):
    return sum(levels)/len(levels)

#create an empty list to store the calculated averages
average_radiations = []

#using a for loop to iterate through the dictionary
for location, levels in locations.items():
    average_radiation = calculate_average(levels)
    print(f"{location} Average Radiation Level : {average_radiation}")
    average_radiations.append(average_radiation) 

    #using numpy to calculate standard deviation
    std_dev = np.std(average_radiations)

    print(f"Standard deviation for {location} : {std_dev}")

#code to get continuous data input using while loop
measurements =[]

#Debugging: informing the user that data entry process is starting
print("Begin entering new radiation levels. Type 'done' to finish")

while True:
    level = input("Please start entering radiation levels or 'done' to exit: ")
    if level.lower() == 'done':
        #Debugging: Confirm that the loop exit condition has been met
        print("Exiting loop")
        break
    
    try:
        
        measurements.append(int(level))
        
        print(f"Added level : {level}")
        print(measurements)
    
    except ValueError:
        
        print("Invalid input. Please enter a number or 'done'.")

#After exiting the loop, calculate and display the average of the new measurements
if measurements:
    average = sum(measurements)/len(measurements)
    print(f"New measurements Average Radiation Level : {average}")

else:
    print("Debug : No new measurements were entered")

