import random as rd
import slowSorts
import recursiveSorts

def main():
    myList = rd.sample(range(1000),1000)
    #myList = [3,2,1,7,5,8,4,6,10,9]
    print(myList)
    insertionSortList = myList
    comparisons = slowSorts.insertionSort(insertionSortList)
    print(insertionSortList)
    print("comparisons:",comparisons)

    selectionSortList = myList
    comparisons = slowSorts.selectionSort(selectionSortList)
    print(selectionSortList)
    print("comparisons:",comparisons)

    bubbleSortList = myList
    comparisons = slowSorts.bubbleSort(bubbleSortList)
    print(bubbleSortList)
    print("comparisons:",comparisons)

    mergeSortList = myList
    comparisons = recursiveSorts.mergeSort(mergeSortList)
    print(mergeSortList)
    print("comparisons:",comparisons)
main()
