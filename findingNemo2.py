from timeit import default_timer as timer # time pkg's
from datetime import timedelta            # time pkg's

nemo = ['nemo']     # constant assignment
everyone = ['dory','bruce','marlin','nemo','gill','bloat','nigel','squirt','darla','hank'] # constant assignment

def largeArray(array):   # Function to copy the array multiple times.
    largelist = []       # define an empty list
    for i in range(50):  # expanding the list 50 times
        largelist.extend(array)
    
    return largelist
    

def findNemo(array):     # Function to find Nemo
    start = timer()    
    for i in range(len(array)):
        if array[i] == 'nemo':
            print('Found NEMO!')
    end = timer()
    print('Call to find Nemo took ' + str(timedelta(seconds = end-start)) + ' milliseconds')

findNemo(everyone)
findNemo(largeArray(everyone))

