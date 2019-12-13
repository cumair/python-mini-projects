'''

Write a class SixSidedDie. The class should include the following methods:
roll(), getFaceValue(), and __repr__().

Create a TenSidedDie and a TwentySidedDie class. These two class must extend SixSidedDie.
They must provide the same functionality. They must not re-implement any code that is not necessary.

Create a Cup class. A cup will hold several dice that may be rolled at once.
The cup may hold any number of six-, ten-, or twenty- sided dice.

The Cup class should include the following functionality: roll(), getSum(), __repr__().

'''

import random

# *******************************************************************

class SixSidedDie:
    'A blueprint for SixSidedDie roll'

    def roll(self):
        'rolls dice and return a value b/w 1 to 6 randomly'
        self.num = random.randint(1,6)          #generate a random integer b/w 1-6
        return self.num                         #return random int

    def getFaceValue(self):
        'returns the face value of die'
        return self.num                         #return face value

    def __repr__(self):
        'gives canonical representation of die'
        return 'SixSidedDie({})'.format(self.num)

# *******************************************************************

class TenSidedDie(SixSidedDie):                 #class TenSidedDie inherits SixSidedDie
    'A blueprint for TenSidedDie roll'

    def roll(self):
        'rolls dice and return a value b/w 1 to 10 randomly'
        self.num = random.randint(1,10)         #generate a random integer b/w 1-10
        return self.num                         #return random int

    def __repr__(self):
        'gives canonical representation of die'
        return 'TenSidedDie({})'.format(self.num)

# *******************************************************************

class TwentySidedDie(SixSidedDie):              #class TwentySidedDie inherits SixSidedDie
    'A blueprint for TwentySidedDie roll'

    def roll(self):
        'rolls dice and return a value b/w 1 to 20 randomly'
        self.num = random.randint(1,20)         #generate a random integer b/w 1-20
        return self.num                         #return random int

    def __repr__(self):
        'gives canonical representation of die'
        return 'TwentySidedDie({})'.format(self.num)

# *******************************************************************

class Cup:
    'A class that holds several dice, rolled at once, and get sum'

    def __init__(self, six=1, ten=1, twenty=1):     #By default, the cup will contain one of each type of die
        'initializer for cup holding several dice'

        self.six = six
        self.ten = ten
        self.twenty = twenty

        self.cup = []                               #empty list

        for i in range(self.six):
            die = SixSidedDie()                     #contains a reference to a SixSidedDie object
            self.cup.append(die)                    #append face value of SixSidedDie in cup

        for i in range(self.ten):
            die = TenSidedDie()                     #contains a reference to a TenSidedDie object
            self.cup.append(die)                    #append face value of TenSidedDie in cup

        for i in range(self.twenty):
            die = TwentySidedDie()                  #contains a reference to a TwentySidedDie object
            self.cup.append(die)                    #append face value of TwentySidedDie in cup

          
    def roll(self):
        'rolls all dice in a cup and return a list of values'
        
        self.vals = []                              #empty list for values
        
        for die in self.cup:                        #for loop in self.cup
            self.vals.append(die.roll())
        return self.vals


    def getSum(self):                               #get sum of rolls
        'returns the sum of rolls'
        return sum(self.vals)


    def __repr__(self):
        'gives canonical representation of cup'
        return 'Cup({})'.format(tuple(self.cup))


# *******************************************************************

def test_cases():                                   #display test cases
    'print test cases'
    
    cup0 = Cup(1,1,1)
    print('Random Rolls: ',cup0.roll())
    print('Sum of Rolls: ',cup0.getSum())
    print('Cup Contains: ',cup0)
    print('')

    cup1 = Cup(3,0,0)
    print('Random Rolls: ',cup1.roll())
    print('Sum of Rolls: ',cup1.getSum())
    print('Cup Contains: ',cup1)
    print('')

    cup2 = Cup()
    print('Random Rolls: ',cup2.roll())
    print('Sum of Rolls: ',cup2.getSum())
    print('Cup Contains: ',cup2)
    print('')

    cup3 = Cup(1,2,1)
    print('Random Rolls: ',cup3.roll())
    print('Sum of Rolls: ',cup3.getSum())
    print('Cup Contains: ',cup3)

# *******************************************************************
test_cases()

