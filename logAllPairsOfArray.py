# Log all pairs of array

boxes = ['a','b','c','d','e']

def logAllPairsOfArray(array):
    for i in range(len(boxes)):
        for j in range(len(boxes)):
            print(boxes[i],boxes[j])

logAllPairsOfArray(boxes)