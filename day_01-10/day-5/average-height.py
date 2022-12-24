# Instructions
# You are going to write a program that calculates the average student height from a List of heights.
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
# Example Input
# 156 178 165 171 187
# In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]
# Example Output
# 171

# Declaring variables
grand_total = 0
count_of_heights = 0
average = 0

# Ask user for list of heights and convert it into a list
input_student_height = input('Please enter student height separated by ("_,")---> ')
student_heights_list = input_student_height.split(", ")

# For every height input in the list sum it into a grand total
# and count every loop
for student_height in student_heights_list:
    grand_total += int(student_height)
    count_of_heights += 1
    # print(student_height)
    # print(type(student_height))
    # print(int(student_height))
    # print(type(int(student_height)))
    # print(grand_total)
    # print(count_of_heights)

# Devide grand total by the amount of entries to get the average
average = grand_total / count_of_heights
print(f"The average of student's height is: {round(average, 2)}")