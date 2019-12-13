'''

For this problem you will use the classes from the previous problem diceAndCups to build a game.

The game will work as follows:

1. Greet the user and ask their name.
2. Provide the user with a balance of 100 dollars.
3. Ask them if they would like to play a game.
4. Generate a random number between 1 and 100. This number will be called the goal.
5. Ask the user how much they would like to bet. This money is deducted from their account.
6. Ask the user how many of each die they would like to roll.
7. Create a cup filled with dice according to the user’s input.
8. Roll the cup and display the results.
9. If the roll exactly matches the goal, the user receives 10x bet added to their balance.
10. Otherwise, if the roll is within 3 of the goal but not over, the user receives 5x bet added to their
balance.
11. Otherwise, if the roll is within 10 of the goal but not over, the user receives 2x bet added to their
balance.
12. Report the results to the user. The message should include their name and updated balance.
13. Ask if they would like to play again. If so, go to step 4.

'''

import random
import sys   
from diceAndCups import Cup    #both files should reside under the same path

# *******************************************************************
def main():
    'contains primary loop of the Cups and Dice game'

    greetUser()                                                         #greets and prints rules of the game
    user_name = input('What is your name: ')                            #get user name

    balance = 100                                                       #initial balance is $100
    print('\nHi',user_name,' - You have a balance of:',balance)         #display balance
    
    done = False
    while not done:                                                     #start a while loop
        
        choice = input('\nWould you like to play the game? (y/n): ')    #ask if user would like to play

        if choice == 'y':                                               #continue to game if input is y

            goal = random.randint(1,100)                                #generate a random number b/w 1 and 100
            print('\nYou have a goal of number',goal,'to match\n')      #diplay goal

            bet = user_bet(balance)                                     #get the bet from user
            difference  = get_difference(goal)                          #get difference b/w goal and rolls
            match_calc = multiplier(difference)                         #get multiplier
            
            balance += (bet*match_calc)                                 #get new balance
            print('\n',user_name,':::: Your updated balance is:',balance) #print new balance
            
            if balance == 0:                                            #if user lose all money
                print('\nYou are out of balance\n*****GAME OVER*****')  #display GAME OVER
                done = True                                             #exit out of game
             
        elif choice == 'n':                                             #if input is n
            print('Good Buy!')                                          #display Good Buy
            done = True                                                 #exit the program   

            
# *******************************************************************
def greetUser():
    'Prints an introduction of the program'

    print('''\n********WELCOME TO THE CUPS AND DICE GAME********\n
    Following are the RULES of the game:\n
    -> Player gets a goal to match by rolling cup of dice.
    -> Player get to decide how much they would like to bet 
    -> Player will have to choose how many of each die from
           (Six Sided, Ten Sided, Twenty Sided) they would like to roll.

    -> If the roll exactly matches the goal, you will receive 10x of bet.
    -> If the roll is within 3 of the goal, you will receive 5x of bet.
    -> If the roll is within 10 of the goal, you will receive 2x of bet.
    -> If the roll doesn't match & not within above limits, you will lose the bet.\n''')


# *******************************************************************
def user_bet(balance):
    'gets user input of bet and restricts to enter only a positive number <= balance'

    while True:
        try:
            value = int(input('How much would you like to bet $: '))            #get user input

        except ValueError:                                                      #raise error if user enters anything except a number
            print("ValueError: Please input only a number")
            continue

        if value < 1 or value > balance:                                        #raise error if user enters a negative number OR a number > his balance
            print("InvalidInput: Please input positive number <=",balance)
            continue

        else:
            break #break loop if conditions are met                             #break loop if number is positive and <= balance

    return value                                                                #return bet


# *******************************************************************
def number_of_die(str):
    'gets user input of rolls and restricts to enter only a positive number'

    while True:
        try:
            value = int(input('How many of '+str+' would you like to roll: '))  #get user input

        except ValueError:                                                      #raise error if user enters anything except a number
            print("ValueError: Please input only a number")
            continue

        if value < 0:                                                           #raise error if user enters a number < 0
            print("InvalidInput: Please input a positive number")
            continue

        else:
            break                                                               #break loop if user enters a positive number

    return value                                                                #return number of die


# *******************************************************************
def get_sum_of_rolls():
    'rolls cup of dice and get sum using Cup class'
    
    s = number_of_die('Six Sided Die')                                          #get the number of Six Sided Die
    te = number_of_die('Ten Sided Die')                                         #get the number of Ten Sided Die
    tw = number_of_die('Twenty Sided Die')                                      #get the number of Twenty Sided Die

    cup = Cup(s,te,tw)                                                          #cup contains a reference to a Cup class object
    
    rolls = cup.roll()                                                          #roll the cup 
    summ = cup.getSum()                                                         #get sum of rolls

    print('\nThe sum of rolls is:',summ)                                        #print sum of rolls
    
    return summ                                                                 #return sum of rolls


# *******************************************************************
def get_difference(goal):
    'gets the difference between goal and sum of rolls'
    
    sum_rolls = get_sum_of_rolls()                                              #get sum

    difference = goal - sum_rolls                                               #get difference
    print('The difference between goal and sum of rolls is:',difference)        #print difference
     
    return difference                                                           #return difference


# *******************************************************************
def multiplier(difference):
    'defines multiplier for the the difference b/w goal and sum of rolls'
    
    if difference < 0:                                                          #you lose bet
        return -1                                                               #get -1

    elif difference == 0:                                                       #if roll matches goal 
        return 10                                                               #get 10

    elif difference <= 5:                                                       #if roll within 3 of goal
        return 5                                                                #get 5

    elif difference <= 10:                                                      #if roll within 10 of goal
        return 2                                                                #get 2

    else:                                                                       #you lose bet
        return -1                                                               #get -1


# *******************************************************************
main()

