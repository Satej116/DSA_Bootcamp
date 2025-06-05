def GetData():
    s = input("Enter the String: ").lower()
    return s

def logic(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]

def Long_Pal(s):
    longest = ""
    for i in range(len(s)):
        temp1 = logic(s, i, i)
        temp2 = logic(s, i, i+1)
        if len(temp1) > len(longest):
            longest = temp1
        if len(temp2) > len(longest):
            longest = temp2
    print("Longest Palindromic Substring:", longest)

s = GetData()
Long_Pal(s)
