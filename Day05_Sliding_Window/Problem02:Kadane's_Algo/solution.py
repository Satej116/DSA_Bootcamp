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
        
def Sliding_window(arr,arr_length):
    max_global = arr[0]
    max_current = arr[0]
    
    for i in range(1,arr_length):
        max_current = max(arr[i], max_current + arr[i])
        max_global = max(max_global, max_current)

    print(arr)
    print(max_global)
    
arr, arr_length = GetData()
Sliding_window(arr,arr_length)
