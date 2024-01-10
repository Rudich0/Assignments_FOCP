# Last week you wrote a program that printed out a cheery greeting including your
# name. Take a copy of it, and modify it so that the user enters their name at the
# keyboard, and then receives a greeting. For example:
# Hello, what is your name? Mr Apricot
# Hello, Mr Apricot. Good to meet you!

greeting = input("Hello, what is your name? ")
print(f"Hello, {greeting}. Good to meet you!")

# Write a program that prompts a user to enter a temperature in Celsius, and then
# displays the corresponding temperature in Fahrenheit, like so:
# Enter a temperature in Celsius: 32.5
# 32.5C is equivalent to 90.5F.

temp_in_Celsius = float(input("Enter the temperature in Celsius: "))
temp_in_Fahrenheit = (temp_in_Celsius * 9/5) + 32
print("The temperature in Faharenheit is: ",temp_in_Fahrenheit)

# The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is usually 24 students, but this is
# sometimes varied to create groups of similar size. Write a program that prompts for
# the number of students and group size, and then displays how many groups will be
# needed and how many will be left over in a smaller group.
# How many students? 113
# Required group size? 22
# There will be 5 groups with 3 students left over.
# For bonus credit, see if you can fix the grammar in the output. So if there were 101
# students in groups of 20 the output would be:
# There will be 5 groups with 1 student left over.

no_of_students = int(input("Enter the number of students: "))
required_size = int(input("Enter the required group size: "))

no_of_groups = no_of_students // required_size
left_over = no_of_students % required_size

print(f"There will be {no_of_groups} groups with {left_over} student left over.")

# A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
# first count the sweets and then divide them according to how many pupils attend
# that day. Write a program that will tell the teacher how many sweets to give to each
# pupil, and how many she will have left over.

no_of_sweets = int(input("Enter the number of sweets you have: "))
no_of_students = int(input("Enter the number of students: "))

if no_of_sweets < no_of_students:
    print("!!! Not enought sweets !!!")

else:
    sweets_per_student = no_of_sweets // no_of_students
    remainder = no_of_sweets % no_of_students
    print(f"The students will get {sweets_per_student} number of sweets each and you will have {remainder} number of remaining sweets.")

    