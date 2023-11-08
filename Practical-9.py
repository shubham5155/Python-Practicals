import os
a=open("data.txt","r")
data= a.read()
numofchars=len(data)
numofwords=len(data.split())
numoflines=len(data.splitlines())
print('The number of characters in file are:',numofchars,'\n The number of words in given file are: ',numofwords,'\nThe number of lines in given file are:',numoflines)
