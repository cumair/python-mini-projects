'''
“A stem-and-leaf display or stem-and-leaf plot is a device for presenting quantitative data
in a graphical format, like a histogram, to assist in visualizing the shape of a distribution.
They evolved from Arthur Bowley's work in the early 1900s and are useful tools in exploratory
data analysis. Stemplots became more commonly used in the 1980s after the publication of
John Tukey's book on exploratory data analysis in 1977. The popularity during those years is
attributable to their use of monospaced (typewriter) typestyles that allowed computer technology
of the time to easily produce the graphics. Modern computers' superior graphic capabilities have
meant these techniques are less often used.”
--Wikipedia (retrieved 9/23/2018)

Using three “StemAndLeaf” example datafiles. Consider the following specifications.

a) Greets the user.
b) Asks the user to input a 1, 2 or 3.
c) Given the input, reads in the appropriate datafile and displays a stem-and-leaf plot.
        a. Note: This will require you to make several design decisions.
d) Loops until the user wishes to exit.
'''

from math import sqrt

#*******************************************************
def main(): 
    'main function for Stem And Leaf Plot Implementation'
    done = False
    while not done:
        greetUser()   #call greetUser function
        choice = input('Press y to Continue program or n to Exit program: ') 
        if choice == 'y':  #continue program
            n = getUserInput()
            listOfNum = readFile(n)
            displayStemAndLeaf(listOfNum)
        elif choice == 'n':
            done = True  #exit the program

#*******************************************************          
def greetUser():
    'Prints an introduction to the program'
    print("\nThis program asks the user to input a number 1, 2, or 3.")
    print("Given the input, reads in the appropriate datafile")
    print("and displays a stem-and-leaf plot.")
    print("The program continuous until the user wishes to exit.\n")

#*******************************************************
def getUserInput():
    'gets user input'
    n = ''     #change following directories before running code on your machine
    n1 = "C:/Users/mkalo/Documents/stemANDleaf_datafiles/StemAndLeaf1.txt"
    n2 = "C:/Users/mkalo/Documents/stemANDleaf_datafiles/StemAndLeaf2.txt"
    n3 = "C:/Users/mkalo/Documents/stemANDleaf_datafiles/StemAndLeaf3.txt"

    entry = int(input   #assuming user will only enter 1, 2 or 3
                ('Please enter 1, 2 or 3 for different datafiles: '))  
    if entry == 1:
        n = n1  #reads StemAndLeaf1 
    elif entry == 2:
        n = n2  #reads StemAndLeaf2
    elif entry == 3:
        n = n3  #reads StemAndLeaf3
    return n

#*******************************************************
def readFile(n):
    'read in the file, returns as a list'
    infile = open(n, "r") #open file
    lineList = infile.readlines() #read each line
    infile.close() #close file

    listOfNum = []  #empty list
    for i in range(0,len(lineList)):
        x = int(lineList[i].strip())
        listOfNum.append(x)   #append datapoints into list

    listOfNum.sort()  #sort the list
    return listOfNum  #returns a sorted list of datapoints

#*******************************************************
def displayStemAndLeaf(listOfNum): 
    'gets a sorted list and displays stem and leaf plot'
    bp = findBreakPoint(listOfNum) #returns breakPoint
    dictionary = splitList(listOfNum, bp) #returns a dictionary
    formatting(dictionary) #displays the result

#*******************************************************
def findBreakPoint(listOfNum):
    'returns break point to split between stems and leaves'
    max_data = max(listOfNum)  
    done = False
    while not done:
        breakPoint = 10 #set default breakPoint to 1 digit in leaf
        getdictionary = splitList(listOfNum, breakPoint) #get dict from splitList function
        listOfKeys = list(getdictionary.keys()) #get all stems from dict and add it to a list
        countNoOfitems = len(listOfKeys) #count length of stems
        if countNoOfitems > (max_data//10): #if length of stems > max number in data divided by 10
            breakPoint = breakPoint*10 #increase the breakPoint to 2 digits in leaf
        else: #go with the default breakPoint 1
            done = True
        return breakPoint

#*******************************************************
def splitList(listOfNum, bp):
    'returns a dictionary with stems as keys and leaves as values'
    temp_dict = {}
    for i in listOfNum: #loop into sorted list of ints
        stems = i // bp 
        leaves = i % bp 
        if stems not in temp_dict: #if stem does not exist in dictionary
            temp_dict[stems] = [] #add stem as key
        temp_dict[stems].append(leaves) #add leaves as list of values
    return temp_dict #returns a dict      

#*******************************************************
def formatting(dictionary):
    'gets a dict and prints stem-and-leaf plot'
    min_stems = min(dictionary.keys()) #min of stems
    max_stems = max(dictionary.keys()) #max of stems
    space = len(str(max_stems))         #number of characters in max stem
    for i in range(min_stems, max_stems+1): #loop in range from min stem to max stem
        if i in dictionary.keys():
            print(str(i).ljust(space) + ' | ' + ' '.join(map(str, dictionary[i])))
        else:
            print(str(i).ljust(space) + ' | ')
            
#*******************************************************
main() #calling main function
