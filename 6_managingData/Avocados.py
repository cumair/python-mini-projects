'''

Find on the D2L a datafile named “avocados.csv” -- Retrieved from Kaggle (9/26/2018).
This data was downloaded from the Hass Avocado Board website in May of 2018 and saved as a single CSV.

a) Define a function that takes a variable name in the form of a string (e.g. “Total Volume”),
reads into memory the values for that variable (but just that variable) and computes the mean using the statistics module.

    mean_SM = readAndComputeMean_SM(“Total Volume”)

b) Define a function that takes a variable name in the form of a string (e.g. “Total Volume”),
reads into memory the values for that variable (but just that variable)
and computes the standard deviation using the statistics module.

    sd_SM = readAndComputeSD_SM(“Total Volume”)

c) Define a function that takes a variable name in the form of a string (e.g. “Total Volume”),
reads into memory the values for that variable (but just that variable)
and computes the median using the statistics module.

    median_SM = readAndComputeMedian_SM(“Total Volume”)

d) Repeat a-c, but instead of using the statistics module write your own “homegrown” code
to compute the mean, standard deviation and median.

    mean_HG = readAndComputeMean_HG(“Total Volume”)
    sd_HG = readAndComputeSD_HG(“Total Volume”)
    median_HG = readAndComputeMedian_HG(“Total Volume”)

e) Repeat a-c, but your functions must be memoryless – you can hold in memory only a single value from the file at any given time.
You may need to keep track of min, max, sum and a handful of counters.

    mean_MML = readAndComputeMean_MML(“Total Volume”)
    sd_MML = readAndComputeSD_MML(“Total Volume”)
    median_MML = readAndComputeMedian_MML(“Total Volume”)

Write test code to demonstrate that the means, standard deviations and medians are the same across all three techniques.
The first 8 functions are trivial. You will not be awarded points for completing them (though you may lose points if you do not.)
The 9th function, “readAndComputeMedian_MML”, is the challenging part.

'''

import statistics
import math
file_name = 'avocado.csv'
var_name = 'Total Volume'

# ************************************************************************
def main():
    'computes and displays mean, standard deviation, & median using different methods'    
    
    SMmean = readAndComputeMean_SM(var_name)
    HGmean = readAndComputeMean_HG(var_name)
    MMLmean = readAndComputeMean_MML(var_name)

    SMSD = readAndComputeSD_SM(var_name)
    HGSD = readAndComputeSD_HG(var_name)
    MMLSD = readAndComputeSD_MML(var_name)

    SMMedian = readAndComputeMedian_SM(var_name)
    HGMedian = readAndComputeMedian_HG(var_name)
    MMLMedian = readAndComputeMedian_MML(var_name)
    
    print('{:20} {:25} {:30} {:35}'.format('METHODS', 'MEAN', 'SD', 'MEDIAN\n'))
    print('{:16} {:20} {:26} {:22}'.format('StatsModule', SMmean, SMSD, SMMedian))
    print('{:17} {:20} {:25} {:22}'.format('Home  Grown', HGmean, HGSD, HGMedian))
    print('{:17} {:20} {:25} {:22}'.format('Memory Less', MMLmean, MMLSD, MMLMedian))

# ************************************************************************
def readFile(var_name):
    'read file and return a list of values for a requested variable'

    lst_values = []                                         #empty list
    infile = open(file_name)                                #open file
    #both avocado.csv and .py file should be saved under same path

    position = infile.readline().split(',').index(var_name) #find position of var_name

    for line in infile.readlines():                         #for every line in file
        lst_values.append(float(line.split(',')[position])) #append values into list
    infile.close()                                          #close file

    return lst_values                                       #return list of values


# **********************STATISTICS MODULE********************************
def readAndComputeMean_SM(var_name):
    'takes a variable name, read file, computes and return mean using SM'

    lst = readFile(var_name)                                #call readFile function to get lst_values
    mean_SM = statistics.mean(lst)                          #calculate mean using SM

    return mean_SM                                          #return SM mean


# ************************************************************************
def readAndComputeSD_SM(var_name):
    'takes a variable name, read file, computes and return SD using SM'

    lst = readFile(var_name)                                #call readFile function to get lst_values
    sd_SM = statistics.pstdev(lst)                          #calculate SD using SM

    return sd_SM                                            #return SM sd


# ************************************************************************
def readAndComputeMedian_SM(var_name):
    'takes a variable name, read file, computes and return median using SM'

    lst = readFile(var_name)                                #call readFile function to get lst_values
    median_SM = statistics.median(lst)                      #calculate median using SM

    return median_SM                                        #return SM median


# *****************************HOMEGROWN***************************
def calcMean_HG(lst):
    'homegrown method to calculate mean, takes a list, return mean'

    summ = 0                                                #keep track of sum
    n = 0                                                   #keep track of n

    for i in lst:                                           #for every iteration in list
        summ += i                                           #add i to summ
        n += 1                                              #increament n by 1

    mean = summ/n                                           #divide summ by n

    return mean                                             #return mean


# ************************************************************************
def readAndComputeMean_HG(var_name):
    'takes a variable name, read file, return mean using calcMean_HG function'

    lst = readFile(var_name)                                #call readFile function to get lst_values
    mean_HG = calcMean_HG(lst)                              #call calcMean_HG function to get mean

    return mean_HG                                          #return HG mean


# ************************************************************************
def readAndComputeSD_HG(var_name):
    'takes a variable name, read file, return SD using homegrown code'

    lst = readFile(var_name)                                #call readFile function to get lst_values
    mean_HG = calcMean_HG(lst)                              #call calcMean_HG function to get mean

    summ = 0                                                #keep track of sum of squared difference
    n = 0                                                   #keep track of n

    for i in lst:                                           #for every iteration in list
        summ += ((mean_HG - i)**2)                          #add squared difference to summ
        n += 1                                              #increament n by 1

    get_variance = summ / n                                 #get variance
    sd_HG = get_variance**.5                                #get sd using HG code

    return sd_HG                                            #return HG sd
    

# ************************************************************************
def readAndComputeMedian_HG(var_name):
    'takes a variable name, read file, return median using homegrown code'

    lst = readFile(var_name)                                #call readFile function to get lst_values
    lst.sort()                                              #sort list
    length_lst = len(lst)                                   #get length of a list

    if length_lst % 2 == 1:                                 #if list has odd number of items
        midpoint = length_lst//2                            #get midpoint index
        median_HG = lst[midpoint]                           #median is middle index number in list

    else:                                                   #if list has even number of items
        mid_1 = length_lst//2                               #get 1st midpoint
        mid_2 = length_lst//2-1                             #get 2nd midpoint
        median_HG = (lst[mid_1] + lst[mid_2]) / 2           #add 1st and 2nd midpoints in list and / 2
    
    return median_HG                                        #return HG median


# *****************************MEMORYLESS**************************
def readAndComputeMean_MML(var_name):
    'takes a variable name, read file, return mean using MML code'
    
    summ = 0                                                        #keep track of sum
    n = 0                                                           #keep track of n

    infile = open(file_name)                                        #open file
    #both avocado.csv and .py file should be saved under same path

    read = infile.readline().split(',')                             #readline and split on ','
    position = read.index(var_name)                                 #find position of var_name
    
    done = False
    while not done:                                                 #start while loop
        
        try:
            summ += float(infile.readline().split(',')[position])   #read and add to sum
            n += 1                                                  #increament n by 1

        except:
            infile.close()                                          #close file
            done = True                                             #stop while loop

    mean_MML = (summ/n)                                             #divide sum by n

    return mean_MML                                                 #return MML mean


# ************************************************************************
def readAndComputeSD_MML(var_name):
    'takes a variable name, read file, return SD using MML code'
    
    summ = 0                                                        #keep track of sum of squared difference
    n = 0                                                           #keep track of n

    infile = open(file_name)                                        #open file
    #both avocado.csv and .py file should be saved under same path

    read = infile.readline().split(',')                             #readline and split on ','
    position = read.index(var_name)                                 #find position of var_name
    mean_MML = readAndComputeMean_MML(var_name)                     #call readAndComputeMean_MML function to get mean
    
    done = False
    while not done:                                                 #start while loop
        
        try:
            var = mean_MML - (float(infile.readline().split(',')[position]))
            summ += var**2
            n += 1                                                  #increament n by 1

        except:
            infile.close()                                          #close file
            done = True                                             #stop while loop

    get_variance = summ / n                                         #divide sum by n
    sd_MML = get_variance**.5                                       #get sd using MML

    return sd_MML                                                   #return MML SD


# ************************************************************************
def get_min_max_n(var_name):
    'returns min, max, and n for var_name in file'

    infile = open(file_name)                                        #open file
    read = infile.readline().split(',')                             #readline and split on ','
    position = read.index(var_name)                                 #find position of var_name

    minimum = float(infile.readline().split(',')[position])         #keep track of minimum
    maximum = float(infile.readline().split(',')[position])         #keep track of maximum
    n = 0                                                           #keep track of n

    done = False
    while not done:                                                 #start while loop

        try:
            val = float(infile.readline().split(',')[position])
            
            if val < minimum:                                       #if value < minimum
                minimum = val                                       #set value as new minimum
                
            if val > maximum:                                       #if value > maximum
                maximum = val                                       #set value as new maximum
                
            n += 1                                                  #increament n by 1

        except:
            infile.close()                                          #close file                              
            done = True                                             #stop while loop

    return minimum, maximum, n                                      #return min, max, n


# ************************************************************************
def bins_bounds(minimum, maximum, n):
    'returns 5 bins as lists with low and high limits'
    bin_size = (maximum - minimum)/5                                #size of bin
    
    bin1 = [minimum, minimum + bin_size]                            #1st bin with low and high bounds
    bin2 = [bin1[1], bin1[1] + bin_size]                            #2nd bin with low and high bounds
    bin3 = [bin2[1], bin2[1] + bin_size]                            #3rd bin with low and high bounds
    bin4 = [bin3[1], bin3[1] + bin_size]                            #4th bin with low and high bounds
    bin5 = [bin4[1], maximum + 1]                                   #5th bin with low and high bounds

    return bin1,bin2,bin3,bin4,bin5


# ************************************************************************
def counters(var_name, n, bin1, bin2, bin3, bin4, bin5):
    'returns list of counters'
    
    lst = [0,0,0,0,0,0,0]                                           #list to keep track of counters

    infile = open(file_name)                                        #open file
    read = infile.readline().split(',')                             #readline and split on ','
    position = read.index(var_name)                                 #find position of var_name

    for i in range(n):                                              #for loop in range of n
        val = float(infile.readline().split(',')[position])         #read header and find index for var_name

        if val < bin1[0]:
            lst[0] += 1
        if val >= bin1[0] and val < bin1[1]:
            lst[1] += 1
        if val >= bin2[0] and val < bin2[1]:
            lst[2] += 1
        if val >= bin3[0] and val < bin3[1]:
            lst[3] += 1
        if val >= bin4[0] and val < bin4[1]:
            lst[4] += 1
        if val >= bin5[0] and val < bin5[1]:
            lst[5] += 1
        if val >= bin5[1]:
            lst[6] += 1

    return lst                                                      #lst contains low, 5 bins, high
    infile.close()


# ************************************************************************
def midPoint(minimum, maximum, var_name):
    'returns bin which contains the median'

    mini,maxi,n = get_min_max_n(var_name)                           #call get_min_max_n function
    bin1,bin2,bin3,bin4,bin5 = bins_bounds(minimum, maximum, n)     #call bins_bounds function
    lst = counters(var_name, n, bin1, bin2, bin3, bin4, bin5)       #call counters function

    halfOfn = n//2                                                  #n divided by 2

    if lst[0] + lst[1] > halfOfn:                                   #if low+bin1 > n/2
        return bin1, lst[1]
    elif lst[0] + lst[1] + lst[2] > halfOfn:
        return bin2, lst[2]
    elif lst[0] + lst[1] + lst[2] + lst[3] > halfOfn:
        return bin3, lst[3]
    elif lst[0] + lst[1] + lst[2] + lst[3] + lst[4] > halfOfn:
        return bin4, lst[4]
    else:
        return bin5, lst[5]


# ************************************************************************
def readAndComputeMedian_MML(var_name):
    'takes a variable name, read file, return median using MML code'
    
    minimum, maximum, n = get_min_max_n(var_name)                   #call get_min_max_n function
    binn, count = midPoint(minimum, maximum, var_name)              #call midPoint function

    while count > 1:                                                #start a while loop
        binn, count = midPoint(binn[0], binn[1], var_name)

    infile = open(file_name)                                        #open file
    read = infile.readline().split(',')                             #readline and split on ','
    position = read.index(var_name)                                 #find position of var_name
    
    for i in range(n):
        mid = float(infile.readline().split(',')[position])         #read header and find index for var_name
        if mid >= binn[0] and mid < binn[1]:
            return mid

    infile.close()


# ************************************************************************
main()
