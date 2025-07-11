def GetData():
    arr = []
    
    try:
        while True:
            arr_length = int(input("Enter the Length of Array = "))
            if arr_length > 1:
                try:
                    print("Enter elements in the array:")
                    for i in range(arr_length):
                        val = int(input(f"Element {i+1}: "))
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


def maj_Element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate


if __name__ == "__main__":
    nums, length = GetData()
    if nums:
        result = maj_Element(nums)
        print("\nMajority Element is:", result)