def GetData():
    arr = []
    
    try:
        while True:
            arr_length = int(input("Enter the Length of arr = "))
            if arr_length > 1:
                try:
                    print("Enter elements in the arr:\n")
                    for i in range(arr_length):
                        val = int(input())
                        arr.append(val)
                    print("arr =", arr)
                    break
                except:
                    print("Enter Numerical values only")
            else:
                print("Length must be a positive number and greater than 1. Please try again.")
            
        return arr, arr_length

    except:
        print("Enter only numerical values")
        
def moveZeros(arr,arr_length):

    result = [0] * arr_length
    index = 0  

    
    for i in range(arr_length):
        if arr[i] != 0:
            result[index] = arr[i]
            index += 1

    
    for i in range(index):
        for j in range(0, index - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    
    
    print("After modification arr =", result)





arr, arr_length = GetData()
moveZeros(arr, arr_length)

