#function that convert miles to feet
def miles_to_feet(miles):
    feet = 5280*miles
    return feet
print miles_to_feet(57)
    
#perimeter of a rectangle
def rectangle_perimeter(width, height):
    perimeter = 2*(width+height)
    return perimeter
print "perimeter is " + str(rectangle_perimeter(2,5))

#total number of seconds from hours, minutes and seconds
def total_seconds(hours, minutes, seconds):
    total_nr_seconds = (hours * 3600) + (minutes * 60) + seconds
    return total_nr_seconds
print total_seconds(1,2,3)

#circumference of a circle
import math
def circle_circumference(radius):
    area = math.pi * (radius*radius)
    return area
print circle_circumference(2)

#name and age
def name_tag(first_name, last_name):
    #using string formatting
    return "My name is %s %s" %(first_name, last_name)
print name_tag('George', 'Ciprian')

#print digits of a random number
import random
def print_digits(num):
    return "The tens digit is %d, and the ones digit is %d" %(num//10, num%10)   
#generate a number between 0 and 99
number_generated = random.randrange(0,100)
print "Number is " + str(number_generated) + " ; " + print_digits(number_generated)
