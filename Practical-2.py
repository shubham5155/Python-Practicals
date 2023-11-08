#Program to check whether a number is prime or not


a=int(input('Enter the number that you want to check:'))
if (a>=1):
    for i in range(2,a):
        if(a%i==0):
            print(a,'is not a prime number')
            break
    else:
        print(a,'is a prime number')
else:
    print(a,"is not a prime number")
    
    
    
#Gernerating  prime number till between two intervals; 


a=int(input('Enter the first interval : '))
b=int(input('Enter the second interval : '))

print('The prime number in the given range are:')

for number in range(a, b + 1):
   if (number>1):
         for i in range(2,number):
          if (number%i==0):
            break
         else:
           print(number)
           
           
#Genrating prime numbers till n(any given value)

a=1
b=int(input('Enter the number upto which you want to print prime numberes:'))


for number in range(a, b+1):
   if (number>1):
         for i in range(2,number):
          if (number%i==0):
            break
         else:
           print(number)



