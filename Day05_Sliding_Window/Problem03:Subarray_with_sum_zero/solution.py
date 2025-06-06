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
        
def Sumzero(arr,arr_length):
    
    for k in range(arr_length):
        if (arr[k]==0):
            print(True)
            break

    else:
        for j in range(arr_length):
            for i in range(j+1,arr_length):
                temp = 0
                for k in range(j, i):
                    temp += arr[k]
                if (temp == 0):
                    print(arr[j:i])
                    print(True)
                    return
        else:
            print(False)
                
arr, arr_length = GetData()
Sumzero(arr,arr_length)
