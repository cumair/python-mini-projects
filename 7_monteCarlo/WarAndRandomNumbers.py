'''

Find on the D2L a text version of War and Peace by Leo Tolstoy.
You will use it create a pseudo random number generator. The PRNG should be an object:

    prng = WarAndPeacePseudoRandomNumberGenerator()

Alternatively, you should be able to pass a seed when you create the object:

    prng = WarAndPeacePseudoRandomNumberGenerator(12345)

Then, you should be able to generate pseudo random numbers [0,1):

    r = prng.random()

'''


import statistics

#****************************************************************************
def main():
    'main program for War and Random Numbers'
    
    prngs = int(input('Enter number of prngs to be generated: '))
    seed = int(input('Enter seed value: '))

    print('Thinking...plz wait while the program runs')

    lst_psuedo = lst_psuedoRandom(prngs,seed)
    print('')
    print('List of Psuedo Random Numbers:\n',lst_psuedo)
    print('')
    minMaxMean(lst_psuedo)

#****************************************************************************
def getChars(seed):
    'read file and return a list of random 64 ASCII converted characters'

    infile = open('war-and-peace.txt')                     #open file
    #both war-and-peace.txt and .py file should be saved under same path

    infile.seek(seed)
    read = infile.read()

    chars = []                                             #empty list
    counter = 0

    for char in read:
        if len(chars) < 64:
            counter += 1
            if counter == 100:
                chars.append(ord(char))
                counter = 0

    infile.close()
    return chars

#****************************************************************************
def getRandom(chars):
    'takes a list of chars, returns a list of 32 zeros and ones'

    m = []
    
    for i in range(0,len(chars),2):
        if chars[i] < chars[i+1]:
            m.append(0)
        else:
            m.append(1) 

    return m

#****************************************************************************
def getPsuedoRandom(m):
    'takes a list of 32 zeros and ones, returns a Psuedo Random Number'

    d = [0.5]
    mXd = []

    for i in range(31):
        d.append(d[i]/2)

    for i in range(0,len(m)):
        mXd.append(m[i]*d[i])

    return sum(mXd)

#****************************************************************************
def lst_psuedoRandom(n, seed):
    'gets n and seed value and returns a list of prngs'
    
    lst_psuedoRandom = []
    
    for i in range(n):
        chars = getChars(5000+seed+i)
        m = getRandom(chars)
        psuedoRandom = getPsuedoRandom(m)

        lst_psuedoRandom.append(psuedoRandom)

    return lst_psuedoRandom

#****************************************************************************
def minMaxMean(lst_psuedoRandom):
    'displays min, max, and mean of prngs'
    
    print('Minimum of prngs: ', min(lst_psuedoRandom))
    print('Maximum of prngs: ', max(lst_psuedoRandom))
    print('Mean of prngs: ', statistics.mean(lst_psuedoRandom))


#****************************************************************************
main()
