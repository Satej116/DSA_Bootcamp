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
        
def InsertionSort(arr, arr_length):
    
        for i in range (arr_length):
            key = arr[i]
            j = i - 1

            while(j>=0 and arr[j]>key):
                arr[j+1] = arr[j]
                j-=1
            arr[j+1] = key
        
        print(arr)



arr, arr_length = GetData()
InsertionSort(arr, arr_length)

