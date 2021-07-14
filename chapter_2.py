#chapter_2.py
##Chapter 2 For loops

#for i in range(1,10):
#	print(i)
#	print('Hello')

#for x in range(10):
#	print(x)
import numpy as np
#for x in range(10,1,-1):
#	print(x)
#
#y=np.array([0,0,0,0,0])
#print(y)



#2.5 Exercise
#1.
print('My name'*100)

#2.
for x in range(1,10):
	print('my name')
for x in range(1,10):
	print('my name',end=' ')

#3.
for x in range(100):
	print(x+1,'My name')

#4.
for i in range(1,21):
	print(i,'——',i*i,sep='')

#5.
for x in range(8,90,3):
	print(x,end='	')
print(' ')

#6.
for i in range(100,2,-2):
	print(i,end='	')
print('')

#7.
for i in range(20):
	if i < 5:
		print('A',end='')
	if i >= 5 and i <=10:
		print('B',end='')
	if i >=10  and i <=15:
		print('CD',end='')
	if i > 15 and i <=20:
		print('EFG',end='')
print('')

#8.
#name=input('May I ask you what\'s your name?')
#print_times=eval(input('and how many times do you want your name to be printed?'))
#print('So, your name is %s, and you want your name to be printed %d times.'%(name,print_times))
#print(name*print_times)

##9.
#Fibonacci_number=eval(input('How many Fibonacci number do you want to see?'))
#Fibonacci_x1=1
#Fibonacci_x2=1
#for i in range(1,Fibonacci_number+1):
#	if i<=2:
#		print(Fibonacci_x1,end=' ')
#	elif i>2:
#		Fibonacci_i=Fibonacci_x1+Fibonacci_x2
#		print(Fibonacci_i,end=' ')
#		Fibonacci_x1=Fibonacci_x2
#		Fibonacci_x2=Fibonacci_i
#print('')
#
##10.
#for i in range(4):
#	print('*'*10)
#
##11.
#width=eval(input('Please give me the width of the rectangle:\n'))
#height=eval(input('Please give me the height of the height of the rectangle:\n'))
#for i in range (height):
#	if i==0:
#		print('*'*width)
#	elif i > 0 and i < height-1:
#		print('*',' '*(width-2),'*',sep='')
#	elif i == height-1:
#		print('*'*width)
#
#
##12. 
#width=eval(input('Please give me the width of the rectangle:\n'))
#height=eval(input('Please give me the height of the height of the rectangle:\n'))
#for i in range (height):
#	print('*'*(i+1))
#
#
##13.
#width=eval(input('Please give me the width of the rectangle:\n'))
#height=eval(input('Please give me the height of the height of the rectangle:\n'))
#for i in range (height):
#	print('*'*(width-i))


#14.
diamond_height=eval(input('Please input the diamond height, the height should only be an odd number:\n'))
#i=4
#j=round(diamond_height/2)
#number_of_space=(diamond_height-(2*i-1))/2
#number_of_asterisk=2*i-1
#测试错误行，原因是出现了浮点数
#print(j,number_of_space,number_of_asterisk)
#print(number_of_asterisk,number_of_asterisk)
for i in range(1,diamond_height+1):
	if i <= round(diamond_height/2):
		number_of_space=int((diamond_height-(2*i-1))/2)
		number_of_asterisk=2*i-1
		print(' '*number_of_space,'*'*number_of_asterisk,' '*number_of_space,sep='')
#		print(number_of_space,number_of_asterisk)
	elif i > round(diamond_height/2):
		j=diamond_height-i+1                             #离最后一行的距离，相当于从正向数的第几行
		k=i-round(diamond_height/2)                   #反转成中间行的镜像行
		inverse_diamond_height=round(diamond_height/2)-k
		number_of_space=int((diamond_height-(2*j-1))/2)
		number_of_asterisk=2*j-1
		print(' '*number_of_space,'*'*number_of_asterisk,' '*number_of_space,sep='')
#		print(number_of_space,number_of_asterisk)

#15.final exercise
A_size_height=eval(input('Please input the large A height, the height should only be an odd number:\n'))
width=2*A_size_height-1                                                                                                 #受上一题的灵感，最后一行如果全部是星号则等于width，而每一行如果由*堆积则最后一行星号*的个数就等于width
for i in range(1,A_size_height+1):
	number_of_front_latter_space=int((width-(2*i-1))/2)
	number_of_middle_space=width-number_of_front_latter_space*2-2
	if i == round(A_size_height/2+1):                                                                                     #中间一行的打印有所不同
		print(' '*number_of_front_latter_space,'*'*(number_of_middle_space+2),' '*number_of_front_latter_space,sep='')
	elif i == 1:                                                                                                          #第一行不能打印两个*
		print(' '*number_of_front_latter_space,'*',' '*number_of_front_latter_space,sep='')
	else:
		print(' '*number_of_front_latter_space,'*',' '*number_of_middle_space,'*',' '*number_of_front_latter_space,sep='')





