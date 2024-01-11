# Using command-line arguments involves the sys module. Review the docs for this
# module and using the information in there write a short program that when run
# from the command-line reports what operating system platform is being used

import platform

def get_operating_system():
    system_info = platform.system()
    return system_info

if __name__ == "__main__":
    os = get_operating_system()
    print(f"The operating system is: {os}")


# Write a program that, when run from the command line, reports how many
# arguments were provided. (Remember that the program name itself is not an
# argument).

import sys
value = sys.argv[0: ]
print(f"There are {len(value)} number of arguments.")


# Write a program that takes a bunch of command-line arguments, and then prints
# out the shortest. If there is more than one of the shortest length, any will do.
# Hint: Don't overthink this. A good way to find the shortest is just to sort them.

import sys
new_list = []
value = sys.argv[1:]
new_list.append(value)
new_list.sort()
print("The shortest value is: ",new_list)


# Last week you wrote a program that processed a collection of temperature readings
# entered by the user and displayed the maximum, minimum, and mean. Create a
# version of that program that takes the values from the command-line instead. Be
# sure to handle the case where no arguments are provided!

import sys
from statistics import mean
def get(value):
    try:
        new_list = [float(temperature) for temperature in value]
        
        return new_list
    
    except EOFError:
        print("Invalid input please try again.")

def calculate_max(temp):

    maximum = max(temp)

    return maximum

def calculate_min(temp):

    minimum = min(temp)

    return minimum

def caluculate_mean(temp):
    means = mean(temp)
    return means

def display(max, min, means):
    print("The maximum value is: ",max)
    print("The minimum value is: ",min)
    print("The mean value is: ",means)


if __name__ == "__main__":

    if len(sys.argv ) >= 2:
        value = sys.argv[1:]
        temp = get(value)
        
    else:
        print("Invalid input!!!")

    max = calculate_max(temp)
    min = calculate_min(temp)
    means = caluculate_mean(temp)
    display(max, min, means)


# Write a program that takes the name of a file as a command-line argument, and
# creates a backup copy of that file. The backup should contain an exact copy of the
# contents of the original and should, obviously, have a different name.
# Hint: By now, you should be getting the idea that there is a built-in way to do the
# heavy liing here! Take a look at the "Brief Tour of the Standard Library" in the docs.

import sys
import shutil

def copy_file(file_name):
    '''Copy file from one file to another.'''
    shutil.copyfile(file_name, 'destination.txt')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Invalid input")

    else:
        file_name = sys.argv[1]
    
    copy_file(file_name)