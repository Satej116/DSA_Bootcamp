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
        
def BubbleSort(arr, arr_length):
    
        for j in range(arr_length):
            for k in range(arr_length-j-1):
                if (arr[k]>arr[k+1]):
                    arr[k], arr[k + 1] = arr[k + 1], arr[k]
        print("Sorted Array= ",arr)

        unique_arr = []

        for i in range(len(arr)):
            is_duplicate = False
            for j in range(i):
                if arr[i] == arr[j]:
                    is_duplicate = True
                    break
            if not is_duplicate:
                unique_arr.append(arr[i])

        print("New Array= ",unique_arr)
        print("New Length",len(unique_arr))

arr, arr_length = GetData()
BubbleSort(arr, arr_length)

