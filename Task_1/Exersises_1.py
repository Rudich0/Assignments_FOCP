# Write a program that prints a cheery message (such as "Hello World") on the
# screen. Run it, and note that you have taken the first step to becoming a
# programmer!

print("Hello World")

# Make a copy of the previous program, and modify it so that it displays your name.
# So if your name is Herbert the message should become:
# Hello, Herbert!

print("Hello, Rudich")

# Over the summer, temperatures in Yorkshire reached 38.4C. Write a program that
# converts this value in Celsius to the equivalent temperature in Fahrenheit, and then
# displays both.

Value_in_Celsius = 38.4

Value_in_Fahrenheit =  (9/5 * Value_in_Celsius) + 32

print("Temperatures of Yorkshire in Celsius: ",Value_in_Celsius)
print("Temperatures of Yorkshire in Fahrenheit: ",Value_in_Fahrenheit)

# In a long career for Yorkshire, Geoffrey Boycott played 609 matches, batted 1014
# times, was not out 162 times, and scored 48426 runs. Write a program to calculate
# and display Boycott's batting average.

run_score = 484226
not_out_count = 162
batted_time = 1014

average = int(run_score / (batted_time - not_out_count))
print("Boycott's batting average is: ",average)

# The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is 24 students, since this is the
# number of PCs in a lab. Write a program that calculates how many groups are
# needed for the following number of students: 113, 175, 12. Display how many full
# groups there will be, and how many students will be in the smaller "left over"
# group.

total_students = 113 + 175 + 12

full_groups = total_students // 24
left_over = total_students % 24
print(f"There will be {full_groups} full groups.")
print(f"There will be {left_over} left over students")