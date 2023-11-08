#Program to count frequency of character in a string
x=input('Enter the text in which you want to count: ')
y=input('Enter the letter that you want to count: ')
print(x.count(y))

# #Program to replace a character with another string
x='Ramanujan'
print(x.replace('a','m'))

#Program to remove first occurence of a character from a string
a= input("Enter your text: ")
char = input("Enter the character that you want to delete: ")
result = ' '
for i in range(len(a)):
    if(a[i] == char):
        result= a[0:i] + a[i + 1:len(a)]
        break
print("Entered text       : ",a)
print("Text after removing : ",result)

#Program to remove all occurences of a string
a=input('Enter the text: ')
b=input('Enter the character that you want to remove: ')
print(a.replace(b, ' '))
