# This is the module that controls the light actions.
# import lbraries
import time
from gpiozero import LED

rule = data.split(";")
period = rule(0)
rate = rule(1)
colour1 = rule(2)
action1 = rule(3)
number1 = rule(4)
colour2 = rule(5)
action2 = rule(6)
number2 = rule(7)



# do forever
while true:
    # start of period
    start = time.clock()   
    #do action 1
    show(rate,colour1,action1,number1)
    show(rate,colour2,action2,number2)
    
    time.sleep((start + period - time.clock()))



def show(rate,colour,action,number):
    mycolour = setlightcolour(colour)
    flashlength = setrate(rate)
    doit(mycolour,number,flashlength)
    
    
def doit(colour,number,flashlength):
    while number > 0:
        colour.on
        print("led on")
        time.sleep(flashlength)
        colour.off
        print("led on")
        time.sleep(flashlength)
        number = number - 1
    

def setrate(speed):
    if speed == "slow":
        return 1
    elif speed == "quick":
        return 0.5
    elif speed == "veryquick":
        return 0.2
    elif speed == "ultraquick":
        return 0.05
    return 3





def setlightcolour(colourtoshow):
    # assign pins to coloured leds
    red = LED(17)
    yellow = LED(18)
    green = LED(22)
    blue = LED(23)
    white = LED(24)
    black = LED(17) + LED(18) + LED(22) + LED(23) + LED(24)
    
    if colourtoshow == "red":
        return red
    elif colourtoshow == "green":
        return green
    elif colourtoshow == "yellow":
        return yellow
    elif colourtoshow == "blue":
        return blue
    elif colourtoshow == "white":
        return white
    elif colourtoshow == "black":
        return black
    return

    
