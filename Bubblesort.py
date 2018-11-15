#Bubble Sort Algorithm.

def bubbleSort(myList):
    for i in range (0, len(myList) - 1):
	    for o in range (0, len(myList) - 1 - i):
		    if myList[o] > myList[o+1]:
			    myList[o], myList[o+1] = myList[o+1], myList[o]
	return myList
	
theList = [4, 2, 3, 5, 7, 2 ,4 ,1]
print (bubbleSort (theList))