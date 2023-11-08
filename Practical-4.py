#Program to check whether a givne character is letter,number or special character.
char=input('Enter the character that you want to check:')
if(char>='a' and char<='z') or (char>='A' and char<='Z'):
 print('The given character is a letter.')
elif(char>='0') and (char<='9'):
    print('The given character is a number.')
else:
    print('The given character is a special character')
    
#Program to check if the given character is letter then it is uppercase or lowercase

x=input('Enter the letter that you want to check: ')
if(x>='A' and x<='Z'):
    print('The character is an uppercase letter.')
elif(x>='a' and x<='z'):
    print('The character is a lower case letter.')
else:
    print('The given character is not a letter.')
    
#Program to print number in words
number=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
nty=["","","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninty"]
tens=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
n=int(input("Enter a number "))
if n>99999:
    print("Cant solve for more than 5 digits")
else:
    d=[0,0,0,0,0]
    i=0
    while n>0:
        d[i]=n%10
        i+=1
        n=n//10
    num=""
    if d[4]!=0:
        if(d[4]==1):
            num+=tens[d[3]]+ " Thousand "
        else:
            num+=nty[d[4]]+" "+number[d[3]]+  " Thousand "
    else:
        if d[3]!=0:
            num+=number[d[3]]+ " Thousand "
    if d[2]!=0:
        num+=number[d[2]]+" Hundred "
    if d[1] != 0:
        if (d[1] == 1):
            num += tens[d[0]]
        else:
            num += nty[d[1]] + " " + number[d[0]]
    else:
        if d[0] != 0:
            num += number[d[0]]
    print(num)



