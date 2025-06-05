def GetData():
    s = input("Enter the string: ")
    return s

def compress(s):
    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1]
            if count > 1:
                result += str(count)
            count = 1
            
    result += s[-1]
    if count > 1:
        result += str(count)

    print("Compressed String:", result)
    return result

s = GetData()
compress(s)
