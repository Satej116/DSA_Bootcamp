l = int(input("Enter the Length of Array= "))
count = 0
arr = []
print("Enter only numberical values")

for i in range (0,l):
    val = int(input())
    arr.append(val)
print(arr)

target = int(input("Enter the Target Value = "))

for j in range(0,l):
    if(target == arr[j]):
        print("Index = ",j)
        break
    else:
        count = j

if(count == l-1):
    print("Index = -1")