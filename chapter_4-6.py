#!/bin/python
#chapter_4

#5.
#from random import randint
#random_number=randint(1,10)
#Guess_number=eval(input('Please input the number you guess from 1 to 10:'))
#if Guess_number==random_number:
#	print('Yeh, the number is %d'%random_number)
#else:
#	print('Wrong number')
#
#
#i=0
#if not i:
#	print('I is 0')
#
#
#
#
#
##8.
#year=eval(input('Please input a year:'))
#if year%4==0 and year%100!=0:
#	print('%d is a leap year!'%year)
#elif year%100==0 and year%400!=0:
#	print('%d is not leap year.'%year)
#elif year%400==0:
#	print('%d is a leap year!'%year)


##10.
#from random import randint
#for times in range(10):
#	random_number_1=randint(1,100)
#	random_number_2=randint(1,100)
#	muti_number=eval(input('Please input the result of %d×%d\n'%(random_number_1,random_number_2)))
#	if muti_number==random_number_1*random_number_2:
#		print('Right!')
#	else:
#		print('Wrong, the answer is %d'%(random_number_1*random_number_2))


#12.
#for number in range(1,201):
#	if number%5==2 and number%6==3 and number%7==2:
#		print('%d candies.'%number)
#
#
##chapter 5 Miscellaneous Topics I 杂项专题
#
##flag number 标志数
#num = eval(input('Enter number: '))
#flag = 0
#for i in range(2,num):
#	if num%i==0:
#		flag = 1
#if flag==1:
#	print('Not prime')
#else:
#	print('Prime')
#
###largest number
##largest = eval(input('Enter a positive number: '))
##for i in range(9):
##	num = eval(input('Enter a positive number: '))
##	if num>largest:
##		largest=num
##print('Largest number:', largest)
#
##comments
#from random import randint
#count = 0
#for i in range(10000):
#	num = randint(1, 100)
#	if num%12==0:
#		count=count+1
#print('Number of multiples of 12:', count)
#
#
##5.
#num=eval(input('Please input a  integer number:'))
#sum_divisor=0
#for x in range(1,num+1):
#	if num%x==0:
#		sum_divisor=sum_divisor+num
#print('The sum of the diivisors of %d is %d'%(num,sum_divisor))
#
#
##6.
##find all perferct number between 1 and 10000
#count=0
#for x_range in range(1,1001):
#	sum_divisor=0                            #return to zero
#	for y_divider in range (1,x_range):
#		if x_range%y_divider==0:
#			sum_divisor=sum_divisor+y_divider
#	if sum_divisor==x_range:
#		count+=1
#		print('The %d perfect number is %d'%(count,x_range))
#
#
#	                               
##7.
#from math import sqrt
#num_test=eval(input('Please input a number:'))
#print('Is %d squarefree?'%num_test)
#for x in range(2,round(sqrt(num_test))+1):
#	if num_test%x**2==0:
#		break
#print('Find the first square number:',x)
#print('%d is not squarefree.'%num_test)


#8.swap
x,y,z=4,7,9
print(x,y,z)
x,y,z=y,z,x
print(x,y,z)

i,j,k=12,5,6
print(i,j,k)
i1=i
i=j
j=k
k=i1
print(i,j,k)

#12.guess a random number
from random import randint
x_guess=([2,3,8,7,6])
score=0
for i in range(5):
	randnum=randint(1,10)
	score=score+10 if x_guess[i]==randnum else score-1
	print(randnum)
print('The score is %d'%score)

#14.(a)
#set door num =0,1,2,and the door 3 will win the price
#set 4 counts, count_switch_win,count_switch_goat,count_not_prize,count_not_goat
#use randint to choose door
#如何换门
doors=10
count_switch_win,count_switch_goat,count_not_prize,count_not_goat=0,0,0,0
print(count_switch_win,count_switch_goat,count_not_prize,count_not_goat)

door=range(0,doors)
for i in range(0,10000):
	#choose door
	choose_door=randint(0,doors-1)
#	print(choose_door)
	#将数组中的某一个数去掉
	j=True
	while j==True:
		shut_door=randint(0,doors-1)
#		print(shut_door)
		if shut_door == choose_door or shut_door == door[doors-1]:
			j=True
		else:
			j=False
	#剩余最后一个门的赋值
	j=True
	while j:
		residual_door=randint(0,doors-1)
		if residual_door!=choose_door and residual_door!=shut_door:
			j=False
#	print(choose_door,'-'*5,shut_door,'-'*5,residual_door,sep='')
	if choose_door == door[doors-1]:
		count_not_prize+=1
	elif choose_door != door[doors-1]:
		count_not_goat+=1
	if residual_door == door[doors-1]:                                      #elif要对同一个变量对象吗，这里改为elif就会已知count_switch == 0 
		count_switch_win+=1
	elif residual_door != door[doors-1]:
		count_switch_goat+=1
#	print(choose_door,'-'*5,shut_door,'-'*5,residual_door,'switch_win=',count_switch_win,sep='')
print('The probobility of not switch:',count_not_prize/10000)
print('The probobility of switch:',count_switch_win/10000)
print(count_switch_win,count_switch_goat,count_not_prize,count_not_goat)

#Chapter 6. Strings

string='asfdgyjcbv'
if 'a' in string:
	print('the %s contains cell a'%string)


string_methods='dfgiucxkvjbbkjFAOIUCHJUYI'
print(string_methods.lower())
print(string_methods.upper())
print(string_methods.index('d'))
print(string_methods.count('b'))
print(string_methods.replace('j','J'))
print(string_methods.isalpha())


c_string='I can\'t bbbb'
volume=''
for character in c_string:
	volume=volume+character*2
print(c_string,'\n',volume)




#6.11.1
#这道题还是很有意思的，尤其是The_removed=The_string[1:-1]是一个什么图的逻辑呢
The_string='xdciucghbsdf89987456asfd'
print(len(The_string))
print(The_string*10)
print(The_string[0])
print(The_string[-1])
print(The_string[:3])
print(The_string[-3:])
print(The_string[-1::-1])
print(The_string[7])
#The_removed=(The_string[0]='')+The_string[1:-2]+(The_string[-1]=0)

The_removed=The_string[1:-1]
#The_string=''+The_string[1:-1]+''

print(The_removed)
print(The_string)
print(The_string.upper())
print(The_string.replace('a','e'))
print(The_string.replace('',''))

for c in range(len(The_string)):
	print(The_string[c].isalpha(),The_string[c])
	if The_string[c].isalpha():
		print(The_string[c].isalpha(),The_string[c])
#		The_string[c]=The_string.replace(The_string[c],' ')TypeError: 'str' object does not support item assignment
		The_string=The_string.replace(The_string[c],' ')      #replace等号左边必须是一个字符串
print(The_string)



#
s='asfry643_a'
if s[0].isalpha():
	print('Your string starts with a letter',s[0].isalpha())



#6.11.2
custome_str='I have imput the str, can you gas how many words?'
print(custome_str.count(' ')+1)


#6.11.4
string_4='AKLHsdgiuhx<MBNMqtrweogsip'
for vowels in 'aeiouAEIOU':
	for letter in string_4:
		if letter == vowels:
			print('The str contains vowel')
			break



#6.11.11
string_61111='sdffgsfafdhfujty'
print(string_61111)
locate_a=string_61111.index('a')
print(string_61111[0:locate_a+1])
print(string_61111[locate_a+1:])


#6.11.12
word_12='inputthewordandyoudetermine'
for i in range(1,len(word_12),2):
	letter_upper=word_12[0:i]+word_12[i].upper()+word_12[i+1:]
	print(letter_upper)
	#word_12[i].upper()
	word_12=word_12[0:i]+word_12[i].upper()+word_12[i+1:]          #通过
print(word_12)



#6.11.17
L= [chr(i) for i in range(97,123)]            #这里的i应该是一个局域变量，for循环结束以后就没了
#list_x=range(97,123)
print(L)
print(i)
#print(list_x)
for x in range(4,23):
	print(x)
print(x)
for i in range(26):
	for j in range(26):
		order_num=j+i
		if order_num < 26:
			print(L[order_num],end='')
		elif order_num >= 26:
			print(L[order_num-26],end='')
	print('\n')


#6.11.18
#(a)using count or index
input_str='sdfhfdvasdwqr'
letter1='s'
letter2='5'
isin1=input_str.count(letter1)
isin2=input_str.count(letter2)
print(isin1,isin2)

#(b)still for input_str without count methods, or directly two methods
num1=input_str.count('s')
count=0
for i in input_str:
	if i == 's':
		count+=1
print(num1,count)

#(c)without index, just using for and in


#6.11.21 A good practice, I love this question
from random import randint 
regular_str='Arrini'
length=len(regular_str)
#print(length)
disturb_order=[length]
random_str=''
count=0
while True:
	not_include=True
	random_num=randint(0,length-1)
	#to see if is already included
	#这里根本没运行？
	for k in range(count+1):
		print(k)
		if disturb_order[k]==random_num:
			not_include=False
			print(not_include)
	#still is True that not already included
	if not_include==True:
		random_str=random_str+regular_str[random_num]
		disturb_order.append(random_num)
		print(disturb_order)
		count+=1
	#switch not_include to True
	not_include=True
	if count==length:
		break
print(random_str,count)
print('\n\n')


#6.11.24
#我觉得这题是不是出超纲了，需不需要数字转换成字符
x_power='325x^93'
x_pos=x_power.index('x')
print(x_pos)
caret_pos=x_power.index('^')
print(caret_pos)
pre_exper=eval(x_power[0:x_pos])
power_term=eval(x_power[caret_pos+1:])
derivation_pre=pre_exper*power_term
derivation_power=power_term-1
print(derivation_pre,derivation_power,pre_exper,power_term,sep='	')
print('The derivation is ',derivation_pre,x_power[x_pos],x_power[caret_pos],derivation_power,sep='')
print(x_power[x_pos:caret_pos+1])
print('The derivation is %d%s%d'%(derivation_pre,x_power[x_pos:caret_pos+1],derivation_power))


##6.11.25
##先找到所有数字，或者字母要求对x,y,z,a,b,c,m,n等的都可以
##如果变量数字之后(或者变脸，则需要添加一个*号
##最后一题不好写
#polynomial_25='a+2b+3c+4x+5y+6z+9mn+10'
##polynomial_25_mul=''
#polynomial_25_mul=polynomial_25
#for letter_pos in range(len(polynomial_25)-1):
#	if polynomial_25[letter_pos].isdigit():
#		if polynomial_25[letter_pos+1].isalpha() or polynomial_25[letter_pos+1]=='(':
#			polynomial_25_mul=polynomial_25_mul+polynomial_25[letter_pos]
#
#
#
#
##利用replace
#for arab_letter in '0123456789':
#	#记录下对应阿拉伯数字的位置
#	for letter_pos in range(len(polynomial_25)-1):            #保证不要超过字符串的索引范围
#		if polynomial_25[letter_pos]==arab_letter:
#			if polynomial_25[letter_pos+1]=='(' or polynomial_25[letter_pos+1].isalpha():
#				polynomial_25_mul=polynomial_25_mul.



#chr(i) for i in range(97,123)
polynomial_25='a+2b+3c+4x+5y+6z+9mn+10+8(3x+y)+1030(7788xx+9y)'
Left_parenthesis='('
for digit_num in '0123456789':
	#换26个英文字母
	for i in range(97,123):
		letter_in_poly=chr(i)
		mid_str=digit_num+letter_in_poly
		chg_str=digit_num+'*'+letter_in_poly
		polynomial_25=polynomial_25.replace(mid_str,chg_str)
	#换(
	parenthesis_p=digit_num+Left_parenthesis
	parenthesis_chg=digit_num+'*'+Left_parenthesis
	polynomial_25=polynomial_25.replace(parenthesis_p,parenthesis_chg)
print(polynomial_25)




