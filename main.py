
driver_speed = float (input("Enter your current speed in Km/h: \n")) #The user enters their speed
average_speed = float (input("Enter the allowed average speed in km/h: \n")) # The user enters the average speed acceptable
over_limit = float ((driver_speed-average_speed))/5

if driver_speed < 0 and average_speed < 0: #This ensures that the driver does not enter negative numbers
    print("The speed you have entered is invalid")
elif driver_speed > 0 and driver_speed <= 60: #The speed must be positive numbers and the speed has to be less or equal to 60km/h
    print("OK")# When this condition is true, print OK
elif driver_speed > average_speed and over_limit < 12: # If the speed is over the limit but the demerits less than 12, the points must be printed
    print("The accumulated demerit points are: \n" + str (over_limit))
else:
    print(" It is time to go to jail!") #However, if the points are over 12, this is the feedback.
    answer=10+12
    print(answer);



