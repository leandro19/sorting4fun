def bubbleSort(arr):
    comparisons = 0
    for i in range(0,len(arr)):
    #found online that this could be improved by subtracting i, since the last i elements are already sorted
        for j in range(0,len(arr)-1-i):
            comparisons +=1
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr,comparisons

