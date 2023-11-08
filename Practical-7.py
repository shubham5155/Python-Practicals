#Function that accepts two strings and returns the indices of all occurences of second stirng in the first string as a list

def fdiff(str1, str2):
    
    if str1 == str2:
        return -1
    else:
        for str1, str2 in zip(str1, str2):
            if str1 != str2:
                return str1


string1 = input("Enter first string:")
string2 = input("Enter second string:")
print(fdiff(string1, string2))
    
