def GetData():
    arr = []
    try:
        while True:
            arr_length = int(input("Enter the Length of Array = "))
            if arr_length > 0:
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
                print("Length must be a positive number. Please try again.")
            
        return arr, arr_length

    except:
        print("Enter only numerical values")
        
def Occurences_of_Number(arr, arr_length):
        
    target_value = int(input("Enter the Target Value = "))
    count = 0
    
    for j in range(0,arr_length):
        if target_value == arr[j]:
            count = count + 1
    
    print (count)

arr, arr_length = GetData()
Occurences_of_Number(arr, arr_length)
