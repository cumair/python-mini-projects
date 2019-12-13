'''

A human pyramid is a way of stacking people vertically in a triangle. With the exception of the people in
the bottom row, each person splits their weight evenly on the two people below them in the pyramid. For
example, in the pyramid above, person A splits her weight across people B and C, and person H splits his
weight – plus the accumulated weight of the people he is supporting – onto people L and M. It can be
mighty uncomfortable to be in the bottom row, since you'll have a lot of weight on your back! In this
assignment, you will explore just how much weight that is. Let us assume that everyone in the pyramid
weighs exactly 128 pounds.

Write a recursive function – def humanPyramid(row, column): – that takes as input the row and column
number of a person in a human pyramid, then returns the total weight on that person's back. The row and
column are each zero-indexed, so the person at row 0, column 0 is on top of the pyramid, and person M
in the above picture is at row 4, column 2.

Your implementation of humanPyramid must be implemented recursively and must not use any loops.
You may be surprised how little code is required!

'''

# *******************************************************************
def main():
    'main function for Human Pyramid program'

    greetUser()
    
    done = False
    while not done:         # while loop
        
        choice = input('Press y to Continue program or n to Exit program: ') 
        
        if choice == 'y':  # continue program

            row = get_input('Please enter row number: ')
            column = get_input('Please enter column number: ')
            weight_person = get_input('Please enter weight of a person: ')  # 128 pounds
            
            weight_back = humanPyramid(row,column,weight_person)    # call humanPyramid function
            
            print("The person at row",row,"and column",column,"has total",weight_back,"pounds weight on his back")
        
        elif choice == 'n':
            done = True  # exit the program

#******************************************************************    
def greetUser():
    'Prints an introduction to the program'

    print("This program takes as input the row#, column#, and weight of a person in a human pyramid.")
    print("Given the input, program returns the total weight on that person's back.")
    print("Row# and column# start at 0")
    print("The program uses a recursive function")
    print('')

#*****************************************************************
def get_input(prompt):
    'Prevent code from crashing. This will not allow user to enter anything except a number => 0'

    while True:
        try:
            value = int(input(prompt))

        except ValueError:
            print("ValueError: Please input only a number")
            continue

        if value < 0: # raise below error if input is a negative number
            print("InvalidInput: Please input only a positive number")
            continue

        else:
            break # break loop if conditions are met

    return value


#*****************************************************************
def humanPyramid(row, column, weight):
    'recursive function to return total weight on persons back'

    if row == 0:                # first row
        return 0                # 0 weight on A's back :)

    elif column == 0:           # first column
        return (humanPyramid(row - 1, column, weight) + weight) / 2

    elif column == row:         # last column
        return (humanPyramid(row - 1, column - 1, weight) + weight) / 2

    else:                       # people in the middle :(
        return weight + (humanPyramid(row - 1, column - 1, weight) / 2) + (
                        humanPyramid(row - 1, column, weight) / 2)

#*****************************************************************

main()
