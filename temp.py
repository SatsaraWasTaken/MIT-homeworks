# -*- coding: utf-8 -*-
 
"""
Lecture 1

# Declarative Knowledge: a statement of a fact
# Imperative Knowledge: how to do something (base things)

# Computers differs to 2 section
# 1-Fixed Program Computers: 1940's, Doesn't store dara ex/ pocket calculators
# 2-Stored Program Computers: after 40's, Does store,operate, Instructive
# integers, strings

# Operators
# 1-int(integer): tam sayısını alır ex/ int(5.6) -> 5 turns something to integer

# 2-float: ondalık sayı yapar ex/ float(21) -> 21.0 ex/ float(3.53) -> 3.53

# 3-bool: identify its truability true/false ex/ bool(True) -> True ex/ bool(False) -> False ex/ bool() -> False P.S. Capital letter is the only first letter


#*4-NoneType: makes it a 'none' ex * -----------------------------

# 5-type: checks what type that object has etc. int, float, bool... Ex/ type(3) -> int Ex/ type(4.5) -> float Ex/ type(True) -> bool Ex/ type(str) -> type

# 6-round: rounds the integer sadece tam sayıyı Ex/ round(3.456) -> 3 Ex/ round(4.0053) -> 4

Lecture 1
"""
"""
Lecture 2

# 7-del: deletes variable

# 8-len(length):          Ex/ s='abc' len(s)=3
# 9-character indexing x[y]      012
#                              -3-2-1
#                          s[0]=a s[1]=b s[2]=c
#                          s[-1]=c s[-2]=b s[-3]=a   Ex/ s[len(s)-1]=c (3-1=2)

# 10-print: shows outputs to the user
# print('Hello World for the 9th time!')
# pos_msg1 = '"Do good and good will come to you." —Adam Lowy'
# print(pos_msg1)

# first_name = 'Mustafa'
# second_name = 'Sabri'
# last_name = 'Derbent'
# age = 18
# print(first_name, second_name, last_name)
# print(last_name +" "+str(age))

# 11-str(string): turns int->str  Ex/ str(4) type doesnt change but the way it performs does

# 12-input: gets data from a user in str Ex/ x = input(s)
# username = input("Enter your username:")
# print('Welcome to Sats gang'+" "+username)

# no_g_axe = input('How many OMEGA AXES you have? ')
# print(no_g_axe+'!? You are wealthy!')
# no_g_axe = int(input('How many OMEGA AXES you have?'))
# print('That means you have at least: ')
# print((no_g_axe * 800000000000))

# Homework_1
# text= input('Enter a verb: ')
# print('I can',text,'better than you!')
# print((text+' ')*4+text)

# Homework_2 Newtons Method f(x)=x**3
# y= int(input('3. dereceden kökü alınacak bir tam sayı seçiniz: '))
# t= int(input('Herhangi bir tam sayı giriniz: '))
# print('Girilen sayının kübü:',t**3)
# yeni_t= t-((t**3-y)/((3*t**2)-1))
# print('İlk girilen sayının 3. dereceden kökü tahmini olarak:',yeni_t,'Daha yakın bir cevap için sonucu tam sayı olarak tekrar sisteme giriniz')

Lecture 2
"""
"""
Lecture 1

# MATH x ve y = int
# x+y: toplama (int+int=int, float+float=float)
# x-y: çıkarma (int-int=int, float-float=float)
# x*y: çarpma (int*int=int, float*float=float)
# x/y: bölme (always float)
# x//y: x'in y'ye bölümünün tam sayısı Ex/ 11//3 -> 3
# x%y: x'in y'ye bölümünden kalan
# x**y: x üzeri y 

# variable = value Ex/ pi = 355/113 Ex/ x = 6+1 Ex/ x = 6 Err/ 6 = x

# Binding/Rebinding
# pi = 3.14             info we have, pi=3.14
# radius = 2            info we have, pi=3.14 radius=2
# area = pi*(radius**2) info we have, pi=3.14 radius=2 area=12.56
# radius = radius + 1   info we have, pi=3.14 radius=3 area=12.56
# Q/ x=1 y=10 swap the values of x&y?
# A/ x=1
#    y=10
#    geç=x  >-> Err/ x=geç undefined
#    x=y
#    y=geç
#    del(geç) >-> to delete all del(x, y, geç)

Lecture 1

"""
"""
Lecture 2

# Concatenate
# a="Buse"             using "" or '' makes us use a string to put in
# b='Neburdayız'
# a+b='BuseNeburdayız' to put a blank use " " or ' '
# --- dont_do_it = "akyar" * 4 >-> repeats itself

# Slicing
# if step is + rigth->left    [start:stop:step] >-> [start:stop] step is +1
# if step is - left->rigth
# Ex/ s='abcdefgh'
#        01234567
#     s[3:6]='def'   s[3:6:2]='df' it doesnt include the stop   s[4:1:-2]='ec'
#     s[:]='abcdefgh's[::-1]='hgfedcba'                         s[6:3]= '' because it tries to go rigth but there is no elements there thats why its just blank

# Strings          "x" or 'x'
#   -Immutable Strings (cannot be modified)
#    o=kan
#*   Err/ o[0]='c'    A/ o='c'+o[1:len(o)] >-> changes just the first letter idk why others dont work fn ------------------
# Err/ print(last_name + age)
# A/ print(last_name + str(age))

#   -F Strings:sensitive blanks
#Homework 3 precantage accounting
# a=3000
# b=1/4
# print(a*b,'is', b*100, '% of', a ) #"750.0 is 25.0 % of 3000" >-> to get rid of the space in between the % and the 25 we use f str or str
# print(a*b,'is', str(b*100) +'% of',a) #virgül yerine +
# print(f'{a*b} is {b*100}% of {a}') #hassas boşluklar

# Branching
#   -Comparison (True/False)
#     a > b
#     a >= b 
#     a < b 
#     a <= b 
#     a == b equality test
#     a != b inequality test 
     # 2<3 -> True
     # not 2<3 -> False
     # 2<3 and 3<4 -> True
     # 2<3 or 3>4 -> True
# Homework 4 | Secret Number
# secret_number = 3
# guess=int(input('Enter a number 1-10 to find the answer: '))
# print(secret_number==guess)

#   -If, Elif Else Commands
# sleep = 6.5
# work = 6
# if (sleep+work) >= 24:
#     print('Either you mistyped or need in a better life ma dude!')
# elif (sleep+work) >= 16.5:
#     print('You are very hardworking, keep up!')
# elif (sleep+work) <= 10:
#     print('GET A LIFE')
# else :
#     print('You are livin it!')
# free_time=abs(24-sleep-work)
# print("You've got",free_time,'h of free time')

# Homework 5 | Secret number high or low
# number = 69
# guess = int(input('Guess a Number 1-100: '))
# if (number > guess):
#     print('Higher, try again')
# elif (number < guess):
#     print('Lower, try again')
# else :
#     print('You are correct!')

Lecture 2
    """
"""
Lecture 3

# While Loop
# while <condition>:
#     <code1>
#     <code2>
#        ...

# Homework6 Lost Forest
way_to_go = input('Type a direction you want to go: ')
while way_to_go != 'left' :
    way_to_go = input('Type a direction you want to go: ')
print('Congratualitons! You have made it out!')

# Homework7 | Countdown
x = int(input('Enter a positive integer: '))
if x > 0:
    while x > 0:
        print(x)
        x = x-1
else :
    print('Please enter a positive integer: ')

# Homework8 | Wish granter
wish = input('You have got 3 wishes to be granted. Dont forget you can only grant 1 wish out of time! ')
n = 1
while n < 3:
    print(wish)
    n = n + 1
    wish = input('Whats the next one? ')
    if n >= 3 :
        print('You are out of wishes')

# Homework9 | Factorial
n = int(input('Enter a number to be factoried: '))
i = 1 
f = 1 
while i <= n:
    f *= i
    i += 1
print(f'{n} factorial is {f}')
same as >->
n = int(input('Any number to be factoried: '))
fac=1 
for i in range(1,n+1):
    fac *= i
print(f'{n} factorial is {fac}')

for n in range(5):    # prints 0 1 2 3 4 not 5
    print(n)
# >-> same as
n = 0
while n <5 :
    print(n)
    n += 1

# for a in range(1,4,1):
#     print(a)
# for b in range(1,4,2):
#     print(b*2)
# for c in range(4,0,-1):
#     print("$"*c)
    
# toplam = 0
# for i in range(10):
#     toplam += i
# print(toplam)

# "son = 5
# toplam = 0
# baş = 3
# for i in range(baş,son+1):
#     toplam += i
# print(toplam)"         >-> use print for debugging

Lecture 3
"""
"""
Lecture 4
# 0.9999999999 != 1.0
Lecture 4
# Break
# a = 0
# for i in range(5,11,2):
#     a += i
#     if a == 7:
#         break
#         a += 1 
# print(a)

# tekrar=0
# for i in range(5):
    # i is 0 2 4
#     if i%2==0 :
#         tekrar += 1 
# print(tekrar) >-> to find even numbers
    
#  String Loops
# s='Catherine Micheal Oppenheimer'
# for char in s:
#     if char == "i" or char == "n":
#         print("there is i oder n")
#     same as >->
# for char in s:
#     if char in 'in':
#         print('there is i oder n')

   #Cheer/Speller
# an_letters ="aefhilmnorsxAEFHILMNORSX"
# word= input('The word you want to cheer: ')
# times = int(input('How many times do you want it to cheer? '))
# for w in word :
#     if w in an_letters:  #for the 'an' letters
#         print(f'Give me an {w}')
#     else:  #for the 'a' letters
#         print(f'Give me a {w}')
# print('What does that spell?')
# for i in range(times):
#     print(word,"!")

#Character no
# s="Ali Derbent"
# seen=' '
# for i in s:
#     if i not in seen:
#         seen += i
# print(len(seen)-1)        

# x = int(input('Enter a number to check if its a square number: '))
# tahmin = 0
# neg_flag = False
# if x < 0 :
#     neg_flag = True
# while tahmin**2 < x:
#     tahmin += 1 
# if tahmin**2 == x :
#     print(tahmin, 'is the square root of',x)
# else :
#     print(f'squre root of {x} ,in integer form, doesnt exsist')
#     if neg_flag == True :
#         print(f'did you mean {-x} ?')

# found_flag = False -----------------------------------
# secret_num = 21
# for i in range(1,11) :
#      # i = 1,2,3... 10
#     if i == secret_num:
#         found_flag = True
#         print('found')
# if not found_flag :
#     print('Not found')
    
# cube = int(input('Enter a integer: '))-----------------
# for i in range(abs(cube)+1) :
#     if i**3 >= abs(cube) :
#         break
# if i**3 > abs(cube):
#     print(f'{cube} is not a perfect cube')
# else :
#     if cube < 0 :
#         i == -i
#     print(f'Cube root of {cube} is {i}')
        
# for ali in range(1001):
#     burak = max(ali-40,0)
#     ceyda = ali*2 
#     if ali + burak + ceyda == 1000:
#         print(f'ali {ali} bilet satmış')
#         print(f'burak {burak} bilet satmış')
#         print(f'ceyda {ceyda} bilet satmıştır')
Lecture 4  
"""
"""
Lecture 5
# x = 0
# for i in range(10):
#     x += 0.1
# print(x, '!=', 10*0.1)

# Decimal -> Binary
# num = int(input('Enter a number: '))
# result = ''
# if num < 0:
#     neg_flag = True
#     num = abs(num)
# else :
#     neg_flag = False
# if num == 0:
#    result = '0'
# while num > 0:
#     result = str(num%2) + result
#     num = num//2
# if neg_flag:
#     result = '-' + result
# print(result)

# Decimal -> Binary  floats ---------------------------
# x = float(input('Enter a decimal between 0 and 1: ')) 
# p = 0
# # 2'nin hangi kuvvetiyle tam sayı yapabiliriz? Ex/ 2**p * 3/8(x) = whole num (p=3)
# # A%1 = decimal points (1 bölümden kalanı verir)
# while ((2**p)*x)%1 != 0 :                 
#     print(f'Kalan: {str((2**p)*x - int((2**p)*x))}') #Komple str aldık printlemek için *?
#     p += 1
# #Phase 2 Its now a whole number we can make it to the Binary
# num = int((2**p)*x)
# result = ''
# if num == 0 :
#     result = '0'
# while num > 0:
#     result = str(num%2) + result
#     num = num//2
# #Phase 3 add a '.' to it so it was the same as starting float Ex/ 64/64
# # Tam Olmadı X
# for i in range(p - len(result)):
#     result = '0' + result
# result = result[0:-p] + '.' + result[-p:]
# print(f'Binary represantation of the decimal {str(x)} is {str(result)}')

# Float Binary & Decimals (x,y) y = noktayı nereye koymalı
# (1,1) = 1*2**1 = 2 = 10
# (1,-1) = 1*2**-1 = 0.5 = 0.1
# (125,-2) = 125*2**-2 = 31.25 = 11111.01
#dont use == floats because it's a approxiation to 32 bits 10*-10 

# Karekök Tahmini
# x = int(input('Enter a number: '))
# epsilon = 0.01 
# tahmin_adedi = 0
# tahmin = 0.0
# artış = 0.0001
# while abs(tahmin**2 - x) >= epsilon and tahmin**2 <= x:
#     tahmin += artış
#     tahmin_adedi += 1
# print('Tahmin sayısı:', tahmin_adedi)
# if abs(tahmin**2-x) >= epsilon:
#     print(x, 'için bir karekök bulunamadı.')
# else:
#     print(f'{tahmin}, {x} in kareköküne yakın')
Lecture 5
"""
"""
Lecture 6   
# Bisection Karekök Tahmini
# x = 36
# epsilon = 0.01
# tahmin_adedi = 0
# low = 0.0
# high = x
# if x >= 1:
#     low = 0.0
#     high = x
# else:
#     low = x
#     high = 1.0
# tahmin = (high + low)/2
# while abs(tahmin**2 - x) >= epsilon:
#     if tahmin**2 > x:
#         high = tahmin
#     else :
#         low = tahmin
#     tahmin = (high + low)/2.0
#     tahmin_adedi += 1
# print(f'Tahmin Adedi : {tahmin_adedi} ')
# print(f'{tahmin}, {x} in kareköküne yakın')

# Bisection Küp Tahmini
# cube = 54321  
# epsilon = 0.01
# low = 0
# high = cube
# tahmin = (high+low)/2.0
# tahmin_adedi = 0
# while abs(tahmin**3-cube) >= epsilon :
#     if tahmin**3 > cube:
#         high = tahmin
#     else:
#         low = tahmin
#     tahmin = (high+low)/2.0
#     tahmin_adedi += 1 
# print(f'Tahmin Adedi : {tahmin_adedi} ')
# print(f'{tahmin}, {cube} in küpköküne yakın')   

# Newton-Raphson f(x)= x**2 - kare
# kare = int(input('Enter a whole number to be squarerooted: '))
# epsilon = 0.1
# tahmin = kare/2 
# tahmin_adedi = 0
# while abs(tahmin**2-kare) >= epsilon :
#     tahmin = tahmin - ((tahmin**2 - kare)/(2*tahmin))
#     tahmin_adedi += 1 
# print(f'Tahmin Sayısı: {tahmin_adedi}')
# print(f'Tahmin: {tahmin}')
Lecture 6
"""

# Functions def
# def cift_mi(a):
#     """
#     Checks that the input is odd or even
#     Writing this to be an exe multi-column comment line :p
#     """
#     if a%2 == 0:
#         return True
#     else :
#         return False
# # print(cift_mi(6))
# a = int(input('Enter a whole number: '))
# if cift_mi(a) == True:
#     print(f'{a} is even')
# else :
#     print(f'{a} is odd')
# >->   Ya Da
# for i in range(9998,10001):
#     if cift_mi(i):        #Hiç bir şey yazmazsa 'True'
#         print(i, 'Çift')
#     else:
#         print(i, 'Tek')

# Divide Calculator by def
# n = int(input('Enter a number to be divided: '))
# d = int(input('Enter a number to divide: '))
# def div_by(n,d):
#     if n%d == 0:
#         return True
#     else: 
#         return False
# b = n/d
# print(f'{n}/{d} = {b}')

# Tam Olmadı ----------------
# Tek Sayı Toplama (a,b) 
# a = int(input('1. Sayı: '))
# b = int(input('2. Sayı: '))
# def tek_toplam(a,b):
#     toplam = 0
#     for i in range(a,b+1):
#         if i%2 == 1:
#             toplam += i
#     return toplam    
# print(tek_toplam(a,b))
# Ya Da
# def tek_toplam(a,b):
#     toplam = 0
#     i = a
#     while i <= b:
#         if i%2 == 1:
#             toplam += i
#         i += 1
#     return toplam
# print(tek_toplam(a,b))


a = 34
b = 68
c = -510
root_1 = (-b + (b**2 -4*a*c)**0.5)/2*a
root_2 = (b + (b**2 -4*a*c)**0.5)/2*a

def is_positive(a):
    if a > 0:
        return True
    else:
        return False
    
if is_positive(root_1) and is_positive(root_2) :
    print(f'Positive roots of the equation are: {root_1} and {root_2}')
elif root_1 > root_2 and is_positive(root_1):
    print(root_1)
elif root_2 > root_1 and is_positive(root_2):
    print(root_2)
else:
    print('There are no positive roots of the equation')

#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  
#
#
#  






















