'''
Goldbach's Conjecture is one of the oldest and best-known unsolved problems in number theory
and all of mathematics. It states that every even integer greater than 2 can be expressed
as the sum of two primes. The conjecture has been shown to hold for all integers less than
4 × 10^18, but remains unproven despite considerable effort.

Test Goldbach's Conjecture on for all integers less than one hundred.
For each integer, print out a single line showing how two primes can sum to the integer.

For example:
2 = 1 + 1
4 = 2 + 2
6 = 3 + 3
8 = 3 + 5
…etc.
'''


from math import sqrt

def main():
    'main function for GoldbachConjecture program'
    greet()
    lstPrime = primeNum(100) #lstPrime contains a list of all prime numbers from 2 to 100
    goldConj(lstPrime) #pass the list of primes to goldConj function


def greet():
    'Prints an introduction to the program'
    print("Test Goldbach's Conjecture on for all integers less than one hundred.")
    print("For each integer, print out a single line showing how two primes can sum to the integer.")
    print('')

    
def primeNum(number):
    'Takes an integer and returns a list of all prime numbers from 2 upto that number'
    lstPrime = [] #empty list for storing primes
    for i in range(2, int(number)+1): #range from 2 to number+1
        done = True
        for prime in range(2, int(sqrt(i))+1): #range from 2 to sqrt(i)+1
            if i%prime == 0: 
                done = False
                break
        if done: #if the number is prime
            lstPrime.append(i)  #append it into lstPrime
        
    return lstPrime  #return the list of prime numbers


def goldConj(lst):
    'finds and displays GoldbachConjecture'
    for even in range(4, 101, 2): #iterate over all even numbers from 4 to 100
        for i in range(even//2 + 1): #iterate upto evenNumber/2 
            if i in lst and (even - i) in lst: #check if i is in the list of primes and even-i is also in the list of Prime
                print(even, '=', i, '+', even - i)  #print evenNumber = 1stprimeNumber + 2ndprimeNumber
                break
        
main()
    

