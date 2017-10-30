import timeit as ti
import random as rd
import slowSorts
import recursiveSorts

def main():
    comparisons = 0
    
    #myList = [3,2,1,7,5,8,4,6,10,9]
    myList = rd.sample(range(10000),10000)

    insertionSortList = myList
    #print(myList)
    print("Insertion sort:")
    t= ti.Timer('comparisons = slowSorts.insertionSort(myList)', setup="import random as rd;from __main__ import slowSorts;myList = %s" %myList)
    comparisons = slowSorts.insertionSort(insertionSortList)
    print("Execution time:",t.timeit(1))
    print("comparisons:",comparisons)

    selectionSortList = myList
    print("Selection sort:")
    t= ti.Timer('comparisons = slowSorts.selectionSort(myList)', setup="import random as rd;from __main__ import slowSorts;myList = %s" %myList)
    comparisons = slowSorts.selectionSort(selectionSortList)
    print("Execution time:",t.timeit(1))
    print("comparisons:",comparisons)


    bubbleSortList = myList
    print("Bubble sort:")
    t= ti.Timer('comparisons = slowSorts.bubbleSort(myList)', setup="import random as rd;from __main__ import slowSorts;myList = %s" %myList)
    comparisons = slowSorts.bubbleSort(bubbleSortList)
    print("Execution time:",t.timeit(1))
    print("comparisons:",comparisons)

    mergeSortList = myList
    print("Merge sort:")
    t= ti.Timer('comparisons = recursiveSorts.mergeSort(myList)', setup="import random as rd;from __main__ import recursiveSorts;myList = %s" %myList)
    comparisons = recursiveSorts.mergeSort(mergeSortList)
    print("Execution time:",t.timeit(1))
    print("comparisons:",comparisons)

    quickSortList = myList
    print("Quick sort:")
    t= ti.Timer('comparisons = recursiveSorts.quickSort(myList)', setup="import random as rd;from __main__ import recursiveSorts;myList = %s" %myList)
    comparisons = recursiveSorts.quickSort(quickSortList)
    print("Execution time:",t.timeit(1))
    print("comparisons:",comparisons)

main()
