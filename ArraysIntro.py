# Python doesnt have built in support for Arrays, we need to import a package called array
# Python Arrays supports only numbers, so we will use numbers for this exercise.
import array as ar
arraytest = ar.array('i',[1,2,3,4])

# Display all the values in the array for illustration
for i in range(len(arraytest)):    
    print(arraytest[i])

#push, add an element at the end of the array
arraytest.append(5)

# Display all the values in the array for illustration
print('After push!') 
for i in range(len(arraytest)):   
    print(arraytest[i])

# pop, remove an element at the end of the array
arraytest.pop()

# Display all the values in the array for illustration
print('After pop!') 
for i in range(len(arraytest)):  # evaluate the length of the array and display all the elements of the array
    print(arraytest[i])

# unshift, adds elements at the beginning of the array

arraytest.insert(0,7)

# Display all the values in the array for illustration
print('After Insert!') 
for i in range(len(arraytest)):  # evaluate the length of the array and display all the elements of the array, O(n)
    print(arraytest[i])

# Splice can be achieved with insert in python.
#-------------------------------------------------------------------------
# Python has powerful feature called lists, we will see that in below section with strings
print('-----------Using List Comprehension----------------')
string = ['a','b','c','d','e']

# Display all the values in the array for illustration
for i in range(len(string)):    
    print(string[i])

#push, add an element at the end of the array
string.append('f')

# Display all the values in the array for illustration
print('After append!') 
for i in range(len(string)):    
    print(string[i])

# pop, remove an element at the end of the array
string.pop()

# Display all the values in the array for illustration
print('After pop!') 
for i in range(len(string)):  # evaluate the length of the array and display all the elements of the array
    print(string[i])

# unshift, adds elements at the beginning of the array
string.insert(0,'x')

# Display all the values in the array for illustration
print('After insert!') 
for i in range(len(string)):  # evaluate the length of the array and display all the elements of the array
    print(string[i])