'''

A prime number (or a prime) is a natural number greater than 1 that cannot be formed by multiplying two
smaller natural numbers.

“Happy” has many definitions (even in mathematics). For our purposes, a happy number is a number
defined by the following process: Starting with any positive integer, replace the number by the sum of the
squares of its digits, and repeat the process until the number either equals 1 (where it will stay), or it loops
endlessly in a cycle that does not include 1. Those numbers for which this process ends in 1 are happy
numbers, while those that do not end in 1 are unhappy numbers (or sad numbers). For example, 19 is
happy, as the associated sequence is:

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Write code that endless loops, requesting/accepting an int from the user. Given the input, your code
should print out whether it is a happy prime, sad prime, happy non-prime, or sad non-prime.

'''


from math import sqrt

#*******************************************************************
def main():
    'main function for Happy Primes program'
    greetUser()
    done = False
    while not done:
        choice = input('Press y to Continue program or n to Exit program: ') 
        if choice == 'y':  #continue program
            n = get_input('Please enter a positive integer > 1: ')
            display(n)
        elif choice == 'n':
            done = True  #exit the program

#******************************************************************    
def greetUser():
    'Prints an introduction to the program'
    print("This program requests an integer from the user.")
    print("Given the input, program prints out whether it is a:")
    print("happy prime, sad prime, happy non-prime, or sad non-prime")
    print('')

#*****************************************************************
def get_input(prompt):
    'Prevent code from crashing. This will not allow user to enter anything except an integer > 1'
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("ValueError: Please input only integers")
            continue

        if value < 2: #raise below error if input is < 2
            print("InvalidInput: Please input only integer > 1")
            continue
        else:
            break #break loop if conditions are met
    return value

#*****************************************************************
def prime(num):
    'returns True if num is Prime or False if num is not Prime'
    if num > 1:
        done = True
        for prime in range(2, int(sqrt(num))+1): #range from 2 to sqrt(num)+1
            if num%prime == 0:
                done = False
                break
        return done

#*****************************************************************
def sumOfSquaredDigits(num):
    'returns sum of sqaured digits'
    summ = 0  #set summ default to 0
    for i in range(len(str(num))): #range for number of digits in num
        summ += int((str(num)[i]))**2
    return summ

#****************************************************************
def happy(num):
    'returns True if num is Happy or returns False if num is not Happy'
    digit = num
    setOfSums = set() #set which keeps track of sum of squared numbers
    setOfSums.add(num)  #add num to set
    
    while True: 
        total = sumOfSquaredDigits(digit)   #find sum of squared digits and assign it to total
        if total == 1:
            check = True #happy number
            break #exit out of loop
        elif total in setOfSums: #stop condition. if integer repeats itself in loop
            check = False #sad number
            break #exit out of loop
        else:
            setOfSums.add(total) #add total into setOfSums
            digit = total  #set digit to new sum of squared digit
    return check
        
#**************************************************************
def display(num):
    'Prints the result as happy prime, sad prime, happy non-prime, or sad non-prime'
    if prime(num): #if num is prime
        if happy(num):  #if num is also happy
            print (num, "is a happy prime")
        else: #if num is prime but not happy
            print (num, "is a sad prime")
    else: #if num is not prime
        if happy(num): #if num is happy but not prime
            print (num, "is a happy non-prime")
        else: #if num is not happy
            print (num, "is a sad non-prime")

main()
