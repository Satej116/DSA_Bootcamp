l = int(input("Enter the Length of Array= "))
arr = []


try:
    for i in range (0,l):
        val = int(input())
        arr.append(val)

    arr.sort()
    print("Sorted array:",arr)

    target = int(input("Enter the Target Value = "))

    start = 0
    end = len(arr) - 1


    while start <= end:
        mid = (start + end)//2
        if (target == arr[mid]):
            print(mid)
            break
        elif(target > arr[mid]):
            start = mid + 1
        else:
            end = mid - 1
        
    else:
        print("Index = -1")

except:
    print("Enter only numberical values")