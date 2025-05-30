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
        swaps = 0
        for j in range(arr_length):
            for k in range(arr_length-j-1):
                if (arr[k]>arr[k+1]):
                    swaps = swaps + 1
                    arr[k]=arr[k] + arr[k+1]
                    arr[k+1]=arr[k] - arr[k+1]
                    arr[k]=arr[k] - arr[k+1]
        print("Sorted Array= ",arr)
        print("Swaps = ",swaps)

arr, arr_length = GetData()
BubbleSort(arr, arr_length)