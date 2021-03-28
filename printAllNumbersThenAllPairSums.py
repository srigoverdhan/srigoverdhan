# Print all numbers then all pair sums

def printAllNumbersThenAllPairSums(numbers):
    print('these are the numbers:')
    for i in range(len(numbers)):
        print(numbers[i])
    
    print('these are their sums:')

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(numbers[i]+numbers[j])

# call the function
printAllNumbersThenAllPairSums([1,2,3,4,5])