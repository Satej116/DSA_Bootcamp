def GetData():
        
    input_str1 = input("Enter the String: ").lower()
    s1 = list(input_str1)
    
    return s1

        
def Long_Pal(s1):

    # unique_arr = ''
    right = len(s1) - 1

    for char in range(len(s1)):
        for char2 in range(right,char,-1):
            if s1[char] == s1[char2]:
                temp = s1[char:char2+1]
                if temp == temp[::-1]:
                    print (''.join(temp))
        
        temp = ' '
        right -= 1
        # unique_arr.append(s1[char])
        

        # print("New Array= ",unique_arr)
        

s1 = GetData()
Long_Pal(s1)

