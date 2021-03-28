
nemo = ['nemo']  #define Nemo

def findNemo(array): # function to find and display nemo
    for i in range(len(array)):
        if array[i] == 'nemo':
            print('Found NEMO!')

# call the function 
findNemo(nemo)

