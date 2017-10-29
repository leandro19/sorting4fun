def bubbleSort(arr):
    comparisons = 0
    for i in range(0,len(arr)):
    #found online that this could be improved by subtracting i, since the last i elements are already sorted
        for j in range(0,len(arr)-1-i):
            comparisons +=1
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return comparisons

def insertionSort(arr):
    comparisons = 0
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            comparisons +=1
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return comparisons

def selectionSort(arr):
    '''
    #My first attempt
    minNum = arr[0]
    comparisons = 0
    for i in range(0,len(arr) - 1):
        j = i+1
        while(j < len(arr)):
            comparisons +=1
            if arr[j] < minNum:
                minNum = arr[j]
            j+=1
        arr[i],arr[arr.index(minNum)] = arr[arr.index(minNum)],arr[i]
        minNum = arr[i+1]
    '''
    comparisons = 0
    for i in range(0,len(arr)):
        maxIdx = i
        for j in range(i+1,len(arr)):
            comparisons += 1
            if arr[maxIdx] > arr[j]:
                maxIdx = j
        arr[i],arr[maxIdx] = arr[maxIdx],arr[i]
    return comparisons
