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
    return arr,comparisons
