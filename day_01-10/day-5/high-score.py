
highest_score = 0
student_scores = ""
# input_student_scores = "78 65 89 86 55 91 64 89"

# Ask user for list of scores and create list
input_student_scores = input("\nEnter scores separated by a space \n---> ")
student_scores = input_student_scores.split(" ")
print(type(student_scores))
print(student_scores)

# For every score in str format in the score's list
for str_score in student_scores:
    # Convert score into int 
    int_score = int(str_score)
    # print(f"{int_score}\n")
    # print(type(int_score))

    # If the score is higher than the highest score
    if int_score > highest_score:
        highest_score = int_score # then replace highest_score
        # print(type(highest_score))
        # print(highest_score)

print(f"The highest score is: {highest_score}")