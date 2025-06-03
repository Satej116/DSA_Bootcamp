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
        
        k = int(input("Enter the target number ="))
        subarray = arr[:k]
        max_sum = sum(subarray)

        for i in range(k,arr_length):
            subarray2 = arr[i]-arr[k-i]
            if(subarray2<max_sum):
                print(max_sum)
                break

arr, arr_length = GetData()
BubbleSort(arr, arr_length)

