#chapter 3 exercises of a practical introduction to python programming
#choose some of the exercises to perform

#4.
from random import randint
for i in range(100):
	print(round(randint(100,1000)/100,2),end='	')
print('')

#5.
from random import randint
for i in range(2,52):
	print(randint(1,i),end='	')
print('')

#6.
#x=eval(input('Please enter the first number:'))
#y=eval(input('Please enter the second number:'))
#print(x/y)
#print(x+y)
#print(abs(x-y)/(x+y))
#print(y)
#print('The computation result of |x-y|/(x+y)=%f'%abs((x-y)/(x+y)))

#8.
from math import sin, sinh, cos, cosh, tan, tanh
print(sin(30))
total_seconds=3467
print('convert to ##minutes ## seconds.')
total_minutes=total_seconds//60
residual_seconds=total_seconds%60
print('The total time is %d minutes %d seconds.'%(total_minutes,residual_seconds))

#11.
weight_kilo=73
weight_pound=round(weight_kilo/1.6,1)
print('Weight in pound is %3.1f'%weight_pound)

#14.
from math import sin, cos, tan, pi
angle=eval(input('Please input an angle:\n'))
radian=pi/180*angle
print('sine={0},cosine={1},tangent={2}'.format(sin(radian),cos(radian),tan(radian)))

#15.
from math import sin, pi
for angle in range(0,360,15):
	print('%d——%.4f'%(angle,sin(angle*pi/180)))

#16.
#from math import floor
#C=floor(2021)                        #Century
#Y=2021                           #Year
#m=(15+C-floor(C/4)-floor((8*C+13)/25))%30
#n=(4+C-floor(C/4))%7
#a=Y%4
#b=Y%7
#c=Y%19
#d=(19*c+m)%30
#e=(2*a+4*b+6*d+n)%7


#19.
width=eval(input('Please input the width of the rectangle:'))
height=eval(input('Please input the height of the rectangle:'))
total_numbers=width*height
x=0
for i in range(height):
	for j in range(width):
		print(x%10,end=' ')
		x+=1
	print('')


