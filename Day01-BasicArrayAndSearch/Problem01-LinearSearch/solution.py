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
        
def LinearSearch(arr, arr_length):
        
        target_value = int(input("Enter the Target Value = "))
    
        for j in range(arr_length):
            if target_value == arr[j]:
                print("Index =", j)
                break
        else:
            print("Index = -1")

arr, arr_length = GetData()
LinearSearch(arr, arr_length)

