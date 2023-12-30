'''
Dr. Eleanor, a renowned physicist, is conducting an experiment to measure 
    the average radiation levels in various environments with high amounts of radioactive waste. 
Over several weeks, she collects a vast amount of data from different locations, 
    ranging from urban areas to dense forests. 
She also takes measurements at varying distances from the known sources of the radiation 
    so she is able to account for any background or ambient, naturally occurring radiation. 
Each location has multiple measurements taken at different times of the day to account for variations.
To process this extensive data, Dr. Eleanor needs a program that can efficiently
    handle the numerous measurements. 
The program should allow her to input the radiation measurements for each location 
    and then calculate essential statistical insights. 
These insights include the average radiation level, the standard deviation to understand the variability, 
    and other relevant metrics that can help her identify patterns or anomalies in the data.
Given the repetitive nature of the data input and the calculations required for
    each set of measurements, the program must utilise loops effectively. 
For instance, a for loop can iterate over each location's data set, while nested loops
    can process individual measurements within those sets. 
Additionally, the program should provide an option for Dr. Eleanor to continue inputting data until she
    decides to stop, making use of a while loop.
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
    average_radiation = calculate_average(levels)#call the function and assign the result to a variable
    print(f"{location} Average Radiation Level : {average_radiation}")
    average_radiations.append(average_radiation) #append the result of the function to the empty list

    #using numpy to calculate standard deviation
    std_dev = np.std(average_radiations)

    print(f"Standard deviation for {location} : {std_dev}")

#code to get continuous data input using while loop
measurements =[]

#Debugging: informing the user that data entry process is starting
print("Begin entering new radiation levels. Type 'done' to finish")

#Using while loop which will run until 'done' is entered
while True:
    level = input("Please start entering radiation levels or 'done' to exit: ")
    if level.lower() == 'done':
        #Debugging: Confirm that the loop exit condition has been met
        print("Exiting loop")
        break
    
    try:
        #convert input to an integer and add to the list
        measurements.append(int(level))
        #Debugging: confirm the input has been added
        print(f"Added level : {level}")
        print(measurements)
    
    except ValueError:
        #Debugging: Alert on invalid input
        print("Invalid input. Please enter a number or 'done'.")

#After exiting the loop, calculate and display the average of the new measurements
if measurements:
    average = sum(measurements)/len(measurements)
    print(f"New measurements Average Radiation Level : {average}")

else:
    #Debugging:Inform the user that no new measurements were entered
    print("Debug : No new measurements were entered")

