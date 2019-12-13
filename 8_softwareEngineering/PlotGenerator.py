'''

A story generator or plot generator is a tool that generates basic narratives or plot ideas….The tool may
allow the user to select elements for the narrative, or it may combine them randomly, a specific
variation known as a random plot generator. Such tools can be created for virtually any genre, although
they tend to produce formulaic and hackneyed situations. – Wikipedia, 2019

Create a class called SimplePlotGenerator that when queried for a plot returns “Something happens”.

    >>pg = SimplePlotGenerator()
    >>pg.generate()
    Something happens

Create a class called RandomPlotGenerator that when queried for a plot returns a random plot
produced from the seven files found on the D2L in the form <plot_names>, a <plot_adjectives>
<plot_profesions>, must <plot_verbs> the <plot_adjectives_evil> <plot_villian_job>, <plot_villains>.
RandomPlotGenerator must extend SimplePlotGenerator.

    >>pg = RandomPlotGenerator()
    >>pg.generate()
    Aaliyah Mosley, a abiding alabasterer, must acknowledge the
    assuming assassin, Acheron Redwood.

Create a class called InteractivePlotGenerator that when queried for a plot offers the user a list of five
random plot_names. After the user selects one, the system will offer the user a list of five random
plot_adjectives. Etc. After the user has made all seven selections, InteractivePlotGenerator should
return the final plot. InteractivePlotGenerator must extend SimplePlotGenerator.

This model will be used in the MVC pattern.

'''


import random

file_Names = ['plot_names', 'plot_adjectives', 'plot_profesions', 'plot_verbs', 'plot_adjectives_evil', 'plot_villian_job', 'plot_villains']

# ***********************************************************************
class SimplePlotGenerator(object):
    'class that when queried for a plot returns “Something happens”'
    
    def __init__(self):
        'initializer for the story'
        
        self._plot = " ".join(["\nRANDOM PLOT",
                               "\n{name}, a {adjective} {profession}, must {verb} the {adjective_evil} {villian_job}, {villain}."])

        self._descriptors = {"name": "a plot_name",
                            "adjective": "a plot_adjective",
                            "profession": "a plot_profession",
                            "verb": "a plot_verb",
                            "adjective_evil": "a plot_adjective_evil",
                            "villian_job": "a plot_villian_job",
                            "villain": "a plot_villain"}

    def registerView(self, a):
        'registers a View'
        
        self.view = a
    

    def generate(self):
        'generates a random plot'
    
        print('Something happens')


# ***********************************************************************
class RandomPlotGenerator(SimplePlotGenerator):         #RPG inherits SPG
    'class that when queried for a plot returns a random plot produced from the seven files'

    def generate(self):                                 #overwritten method
        'generates a random plot from seven files'
        
        self._inputs = dict()    

        self.counter = 0                                #set counter to 0

        for key, value in self._descriptors.items():    # for every key,value in dict
            self._inputs[key] = get_random_one(file_Names[self.counter] + '.txt')
            self.counter += 1                           #increament counter by 1

        print(self._plot.format(**self._inputs))
        

# *************************************************************************************************
class InteractivePlotGenerator(SimplePlotGenerator):    # IPG inherits SPG
    'offer the user a list of five random items and user makes selections out of lists'
    
    def generate(self):                                 # overwritten method
        'prompt user for input and generate a random plot from inputs'
        
        self._inputs = dict()
        self.counter = 0                                # set counter to 0

        for key, value in self._descriptors.items():    # for every key,value in dict

            self.lst = get_random_five(file_Names[self.counter]+'.txt')
            self.counter += 1                           # increament counter by 1

            self.get = int(input("Please select " + value + " from the above five options: "))
            self.val = self.lst[self.get]
            
            self._inputs[key] = self.val
            print('')
            

        print(self._plot.format(**self._inputs))
        

# ***********************************************************************
def get_random_one(filename):
    'returns one random item from a filename'
    
    with open(filename) as f:                           # open file
        lines = list(f)                                 # read line by line

    return random.choice(lines).strip()                 # return a random line from a file


# ***********************************************************************
def get_random_five(filename):
    'returns a list of five random items from a filename'
    
    with open(filename) as f:                           # open file
        lines = list(f)                                 # read line by line

    lst = []                                            # initialize empty list
    
    for i in range(5):                                  # five items
        lst.append(random.choice(lines).strip())        # append i in lst

    counter = 0                                         # set counter to 0
    for i in lst:                                       # for every item in list
        print(str(counter) + ' = ' + i)                 # print counter + item
        counter += 1                                    # increament counter by 1
        
    return lst                                          # return list of five random items
     

# ***************************THINGS IMPORVED*****************************
# For the interactive plot generator:
# 1) Asking the user one question at a time.
# 2) Having a number associated with each choice (e.g. The format is like multiple choice questions).
# 3) Letting the user type in a number instead of words.


# ***********************************************************************
# TEST CODE

pg = SimplePlotGenerator()
pg.generate()

pg = RandomPlotGenerator()
pg.generate()

pg = InteractivePlotGenerator()
pg.generate()
