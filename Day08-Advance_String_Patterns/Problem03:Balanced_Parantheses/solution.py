def Get_data():
    string = input("Enter the brackets: ")
    return string

def Valid_para(string):
    parentheses = {'(': ')', '[': ']', '{': '}'}

    if len(string) % 2 != 0:
        print(False)
        return  

    for i in range(0, len(string), 2):  
        char = string[i]
        next_char = string[i + 1]

        if char in parentheses:
            if parentheses[char] != next_char:
                print(False)
                return  
        else:
            print(False)
            return 

    print(True) 

string = Get_data()
Valid_para(string)
