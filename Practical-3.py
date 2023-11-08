# Progarm for  pyramid
rows= int(input("Enter number of you want to print: "))

p=0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while p!=(2*i-1):
        print("* ", end="")
        p += 1
   
    p= 0
    print()
    
#Program for reverse pyramid
rows = int(input("Enter number of rows: "))

for i in range(rows, 1, -1):
    for space in range(0, rows-i):
        print("  ", end="")
    for j in range(i, 2*i-1):
        print("* ", end="")
    for j in range(1, i-1):
        print("* ", end="")
    print()
