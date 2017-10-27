def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def main():
    myList = [9,4,5,2,1,3,8,6,7,10]
    print(myList)
    myList = insertionSort(myList)
    print(myList)
main()



