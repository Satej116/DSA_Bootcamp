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
        
def Frequency_Counter(arr, arr_length):
        counter = {}
    
        for i in range(arr_length):
            if arr[i] not in counter: 
                count = 1
                for j in range(i+1,arr_length):
                    if arr[i] == arr[j]:
                        count = count + 1

                counter[arr[i]] = count

        print("Frequncy Number= ",counter)
        
arr, arr_length = GetData()
Frequency_Counter(arr, arr_length)

