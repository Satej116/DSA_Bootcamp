arr = []

try:
    while True:
        arr_length = int(input("Enter the Length of Array = "))
        if arr_length > 0:
            break
        else:
            print("Length must be a positive number. Please try again.")

    print("Enter elements in the array:\n")
    for i in range(arr_length):
        val = int(input())
        arr.append(val)
    print("Array =", arr)

    target_value = int(input("Enter the Target Value = "))
    
    for j in range(arr_length):
        if target_value == arr[j]:
            print("Index =", j)
            break
    else:
        print("Index = -1")

except ValueError:
    print("Enter only numerical values")
