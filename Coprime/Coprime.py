
def get_input(prompt):
    'Prevent code from crashing. This will not allow user to enter anything except an integer > 0'
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please input only numbers")
            continue

        if value < 1: #raise below error if input is < 1
            print("Please input only number greater than 0")
            continue
        else:
            break #break loop if conditions are met
    return value


def coprime(a,b):
    'determines if the numbers are coprime or not'
    while b > 0:
        a,b = b, a%b
    return a


def menu():
    'informs user on how to exit the program'
    print('Enter 1 to find if two numbers are coprimes')
    print('Enter 2 to exit the program')


def coprime_test_loop():
    'asks the user for two numbers and pass those two numbers to coprime(a,b) and prints the result'
    done = False
    while not done: #starting a while loop
        menu() #calling menu function
        choice = int(input('Please make an entry either 1 or 2: '))
        if choice == 1:
            first_number = get_input('First number: ')
            second_number = get_input('Second number: ')
            print(coprime(first_number, second_number) == 1) #gets true or false
        elif choice == 2:
            done = True
                
coprime_test_loop() #calling loop function 
