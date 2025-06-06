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
        
def Sliding_window(arr):
        
        k = int(input("Enter the target number ="))
        subarray = arr[:k]
        window_sum = sum(subarray)
        max_sum = window_sum

        for i in range(k,len(arr)):
            window_sum += arr[i]-arr[i-k]            
            if(max_sum<window_sum):
                print(window_sum)        
        else:
            print(max_sum)

    

arr, arr_length = GetData()
Sliding_window(arr)

