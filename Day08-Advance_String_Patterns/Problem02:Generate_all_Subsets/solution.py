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
        
        print([])
        for i in range(arr_length):
            for j in range(arr_length+1):
                if arr[i:j]:
                    print(arr[i:j])


arr, arr_length = GetData()
BubbleSort(arr, arr_length)