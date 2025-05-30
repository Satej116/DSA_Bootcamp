def GetData():
    arr = []
    
    try:
        while True:
            arr_length = int(input("Enter the Length of Array = "))
            if arr_length > 1:
                try:
                    print("Enter elements in the array:\n")
                    for i in range(arr_length):
                        val = int(input())
                        arr.append(val)
                    print("Array =", arr)
                    break
                except:
                    print("Enter Numerical values only")
            else:
                print("Length must be a positive number and greater than 1. Please try again.")
            
        return arr, arr_length

    except:
        print("Enter only numerical values")
        
def SelectionSort(arr, arr_length):
    for j in range(arr_length):
        min = j
        for k in range(j+1, arr_length):
            if arr[k] < arr[min]:
                min = k
        arr[j], arr[min] = arr[min], arr[j] 
    print("Sorted Array =", arr)

arr, arr_length = GetData()
SelectionSort(arr, arr_length)