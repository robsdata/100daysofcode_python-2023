# Ask for user input
year = int(input("Please enter a year ---> + "))


# on every year that is evenly divisible by 4 
if (year % 4 == 0):
    # **except** every year that is evenly divisible by 100 
    if (year % 100 == 0):
        # **unless** the year is also evenly divisible by 400
        if (year % 400 == 0):
            print("The year is leap")
        else: 
            print("The year is not leap")
    else: 
        print("The year is leap")
else:
    print("The year is not leap")
