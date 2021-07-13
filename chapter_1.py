#1.8
#1.print
print('*'*20,'\n','*'*20,'\n','*'*20,sep='')
print('*'*20,'\n','*'*20,'\n','*'*20)
print("""
*******************
*******************
*******************
*******************""")

#2.
print('*'*20,'\n','*',' '*18,'*','\n','*',' '*18,'*','\n','*'*20,sep='')

#3.
print('''
*
**
***
****''')

#4.
x=512-282
y=47*48+5

#5.
#i=input('Please enter the 5 character')
#i=eval(i)
#print('The squre of %d is %d'%(i,i**2))

#6.
#i=eval(input('please input a number:'))
#print(i,'——',2*i,'——',3*i,'——',4*i,'——',5*i,sep='')

#7.
#x=eval(input('please tell me how heavy you are:'))
#print('You weigh %d kg and correspond to %d pond'%(x,2.2*x))

#8.
import numpy as np
import math
i=eval(input('Please input a number'))
j=eval(input('Please input another nember'))
k=eval(input('Please input the third number'))
y=0
z=np.array([0,0,0])
for x in 'abc':
	z[y] = y+1
	y+=1
print(z)
total=i+j+k
average=total/3
print('The total and average is %d and %d respectively.'%(total,average))

#9.
i=eval(input('Please input the total bill:'))
j=eval(input('Please tell me how many percent you want to pay on tips:'))
print('The bill is %d and the percent is %d, so you should pay %d for tips.'%(i,j,i*j))

