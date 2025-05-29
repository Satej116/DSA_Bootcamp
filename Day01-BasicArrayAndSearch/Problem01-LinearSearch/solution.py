arr_length = int(input("Enter the Length of Array= "))
arr = []
element_not_found_checkar = 0

try:
    if(arr_length>1):
        for i in range (0, arr_length):
            val = int(input())
            arr.append(val)
        print(arr)
    else:
        print("Length cannot be negative")

    target_value = int(input("Enter the Target Value = "))
    
    for j in range(0, arr_length):
        if(target_value == arr[j]):
            print("Index = ",j)
            break
        else:
            element_not_found_checkar = j

    if(element_not_found_checkar == arr_length-1):
        print("Index = -1")


except:
    print("Enter only numberical values")

