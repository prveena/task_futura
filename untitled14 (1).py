# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PAHisuNJTva5w06T2nVnCvvvgwAPDl78
"""

n=int(input("Enter a number"))

if n==1:
  print("Monday")
elif n==2:
   print("Tuesday")
elif n==3:
  print("Wednesday")
elif n==4:
  print("Thursday")
elif n==5:
   print("Friday")
elif n==6:
   print("Saturday") 
elif n==7:
  print("Sunday")
else:
  print("Invalid input")

r=int(input("Enter a range"))
for i in range(0,r):
  for j in range(0,i+1):
    print('*',end='')
  print('\n')

limit=8
r=65
for i in range(0,7):
  for j in range(0,i+1):
    print(chr(r),end='')
    r=r+1
  print('\n')

l=10
for i in range(l):
  n=1
  for j in range(0,i+1):
    print(n,'\t',end='')
    n=n+1
  print('\n')

n = 6		
for r in range(0,n):
    for c in range(0,n+1):
        if(r==0 and c%3!=0) or (r==1 and c%3==0) or (r-c==2) or (r+c==8):
            print('*',end='  ')    
        
        elif(r==2 and c==1):
          print('v',end='  ')  
        elif(r==2 and c==2):
          print('e',end='  ')    
        elif(r==2 and c==3):
          print('e',end='  ')    
        elif(r==2 and c==4):
          print('n',end='  ')    
        elif(r==2 and c==5):
          print('a',end='  ')    
         
        else:
            print(' ',end='  ')
       
            
    print()