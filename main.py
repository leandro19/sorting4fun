import random as rd
import insertionSort as iS
import selectionSort as sS
import bubbleSort

def main():
    myList = rd.sample(range(1000),1000)
    #myList = [3,2,1,7,5,8,4,6,10,9]
    print(myList)
    insertionSortList,comparisons = iS.insertionSort(myList)
    print(insertionSortList)
    print("comparisons:",comparisons)

    selectionSortList,comparisons = sS.selectionSort(myList)
    print(selectionSortList)
    print("comparisons:",comparisons)

    bubbleSortList,comparisons = bubbleSort.bubbleSort(myList)
    print(bubbleSortList)
    print("comparisons:",comparisons)
main()
