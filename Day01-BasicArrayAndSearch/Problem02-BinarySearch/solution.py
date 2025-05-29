arr = []

def GetData():
    try:
        while True:
            l = int(input("Enter the Length of Array = "))
        if l > 0:
            break
        else:
            print("Length must be a positive number. Please try again.")

    print("Enter the elements:")
    for i in range(l):
        val = int(input(f"Element {i+1}: "))
        arr.append(val)

    arr.sort()
    print("Sorted array:", arr)

    target = int(input("Enter the Target Value = "))

    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            print("Index =", mid)
            break
        elif target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    else:
        print("Index = -1")

except ValueError:
    print("Enter only numerical values.")
