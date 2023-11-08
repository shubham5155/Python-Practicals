a=eval(input('Enter the numbers: '))
if (a%2==0): 
 for i in range(0,1000):
    print(a*a*a)
    break
else:
 print('It is not an even number')
