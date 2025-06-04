def GetData():
        
    input_str1 = input("Enter the String: ").lower()
    input_str2 = input("Enter the String: ").lower()
    s1 = list(input_str1)
    s2 = list(input_str2)
    
    return s1,s2
    
        

def Anagrams(s1,s2):

    if(len(s1)==len(s2)):

        for j in range(len(s1)):
            for k in range(len(s1)-j-1):
                if (s1[k]>s1[k+1]):
                    s1[k], s1[k + 1] = s1[k + 1], s1[k]
        
        for j in range(len(s2)):
            for k in range(len(s2)-j-1):
                if (s2[k]>s2[k+1]):
                    s2[k], s2[k + 1] = s2[k + 1], s2[k]

        if(s1==s2):
            print (True)
        else:
            print (False)
    
    else:
        print(False)

s1,s2= GetData()
Anagrams(s1,s2)
