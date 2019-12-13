'''

Ask the user for i and n. Create a list of i random numbers between 0 and 100.
Determine if two of the numbers sum to n in O(n.log(n)). Output the appropriate results.

Hint: Binary Search.

Warning: look-ups in dictionaries and lists are not free.

Concession: I will let you sort the list using Python’s built in function as a preprocessing step,
not counted toward the efficiency of your algorithm. Besides, merge sort runs in O(n.log(n)).

'''

import random 
    
# *******************************************************************
def main():
    'main function for Goldbach Deuce program'

    greetUser()
    
    done = False
    while not done:         # while loop
        
        choice = input('Press y to Continue program or n to Exit program: ') 
        
        if choice == 'y':  # continue program

            i = get_input('Enter i to create a list of random numbers: ')
            n = get_input('Enter n for the desired sum: ')
            
            lst_num = getList(i)            # get list of i random numbers
            numbers = goldDeuce(lst_num,n)  

            print(numbers)
        
        elif choice == 'n':
            done = True    # exit the program

#******************************************************************    
def greetUser():
    'Prints an introduction of the program'

    print("This program asks the user for i and n.")
    print("Given the input, create a list of i random numbers b/w 0 and 100.")
    print("then using Binary Search, determines if two of the numbers sum to n in time complexity of O nlogn")
    print("and output two numbers which sum to n")
    print('')

#*****************************************************************
def get_input(prompt):
    'Prevent code from crashing. This will not allow user to enter anything except a number > 0'

    while True:
        try:
            value = int(input(prompt))

        except ValueError:
            print("ValueError: Please input only a number")
            continue

        if value < 1: # raise below error if input is a negative number
            print("InvalidInput: Please input only a positive number")
            continue

        else:
            break # break loop if conditions are met

    return value


#*****************************************************************
def getList(i):
    'returns unsorted list of i random numbers'
    lst = []                                #empty list

    for x in range(i):                      
        lst.append(random.randrange(0,101)) #generate and append random numbers in lst        
   
    return lst                              #return list
    

#*****************************************************************
def goldDeuce(i,n):
    'using binary search, determines if two elements in list sum to n'

    lst = list(sorted(i))                   #sorting list. time complexity O (n log n)
    
    low = 0                                 #first index of list
    high = len(lst) - 1                     #last index of list

    while low < high:                       #there is still a range to search
        summ = lst[low] + lst[high]         #add two elements of list

        if summ < n:                        #if sum is < desired n
            low += 1                        #move bottom marker up
        elif summ > n:                      #if sum is > desired n
            high -= 1                       #move top marker down
        else:                               #if sum = desired n
            return lst[low], lst[high]      #found it! Return 1st number, 2nd number

    print('There is no pair which sum to {}'.format(n))    #if no pair is found


#*****************************************************************
main()


