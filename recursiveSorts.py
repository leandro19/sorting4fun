def mergeSort(arr):
    comparisons = 0
    if len(arr) > 1:
        #split the array to two subarrays
        m = len(arr)//2
        leftArr = arr[:m]
        rightArr = arr[m:]

        #recursive call
        comparisons += mergeSort(leftArr)
        comparisons += mergeSort(rightArr)

        #i,j,k are the indices for the left subarray, right subarray, and array respectively
        i,j,k = 0,0,0

        #Loop through the subarrays
        while i < len(leftArr) and j < len(rightArr):
            #check to see if the element of the left array is less than the element of the right one
            #move to the next element of the subarray with the smaller element and the large array and repeat the process
            comparisons +=1
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i +=1
            else:
                arr[k] = rightArr[j]
                j +=1
            k +=1

        #Once one subarray is completely looped through, we need to put in the rest of the elements of the other array
        while i < len(leftArr):
            arr[k] = leftArr[i]
            i+=1

        while j < len(rightArr):
            arr[k] = rightArr[j]
            j+=1
    return comparisons
