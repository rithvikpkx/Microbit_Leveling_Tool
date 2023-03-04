#9.2
#Imports everything from microbit module
from microbit import *

#9.4
#Creates variable named CENTER with value 2
CENTER = 2


#9.2
#Infinite while loop
while True:
    
    #9.2
    #Gets accelerometer data about tilt
    #Assigns this value to variable tilt
    tilt = accelerometer.get_x()
    
    #9.3
    #Divides tilt by 1024 then multiplies by 10
    #Assigns this value to variable scaled
    scaled = (tilt / 1024) * 10
    
    #9.3
    #Converts value of scaled to an integer
    scaled = int(scaled)
    
    #9.4
    #Subtracts scaled from CENTER
    #Assigns this value to variable column
    column = CENTER - scaled
    
    #9.4
    #Conditional If statement
    #Checks if value of column is greater than integer 4
    #If True, runs indented code
    #If False, skips indented code and moves on
    if column > 4:
        
        #9.4
        #Sets value of column to integer 4
        column = 4
        
    #9.4
    #Conditional Else If statement
    #Checks if value of column is less than 0
    #If True, runs indented code
    #If False, skip indented code
    elif column < 0:
        
        #9.4
        #Set value of column to 0
        column = 0
    
    #9.4
    #Clears the display of all things
    #Makes the screen blank
    display.clear()
    
    #9.4
    #Sets one pixel on column number "column" and row to brightness 9 on the microbit LED array
    display.set_pixel(column, 4, 9)
