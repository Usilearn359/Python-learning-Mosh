# What is function and why needed
# Print and return

# def my_fun():
#     print("Hello, World!")
# my_fun()

# def my_func1(name):
#     print(name)
# my_func1('Usman')

# def my_func2(num1,num2):
#     print(num1 + num2)
# result=my_func2(10,20)
# print(result)

# # return
# def my_func2(num1,num2):
#     return num1 + num2
# result=my_func2('10','20')
# print(result)
# print(type(result))

# # check the user guess to find the correct bucket 

# from random import shuffle 
# def my_list(mylist):
#     shuffle(mylist)
#     return mylist
# result=my_list(['','O',''])
# # check the user guess to find the correct bucket
# def user_guess():
#     guess=''
#     while guess not in ['0','1','2']:
#         guess=input('pick a number 0,1,2: ')
#     return int(guess)
# user_guess()

# def check_guess(mylist,guess):
#     if mylist[guess] == 'O':
#         print('correct')
#     else:
#         print('incorrect')

# mylist=['','O','']
# mixedup=my_list(mylist)
# guess=user_guess()
# check_guess(mixedup,guess)

# Arguments and Keyward #Args return tuple while Kwargs return dictionary 
def my_func(*args):
    print(args)
    return sum(args)*0.05 
result=my_func(100,200,300,400,500)
print(result)

def my_func(**kwargs):
    if 'fruit' in kwargs:
        print(kwargs)
        print('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('no fruit')
my_func(fruit='apple')

def my_func(*args,**kwargs):
    print('I would like to eat {} {}'.format(args[1],kwargs['food']))
my_func(10,20,30,40, fruit='banana', drink='juice', food='Pizza ')

def myfunc(*args):
    print(args)
    list_even=[]
    for index in args:
        print(index)
        if index%2==0:
            list_even.append(index)
    return list_even
    
result= myfunc(1,2,10,13,100,20,5,21,30)
print(result)

# def myfunc(*args):
#     a=args.split()
#     out=''
#     i=0
#     for letter in a:
#         print(letter[i])
#         if letter[i]%2 ==0 :
#             letter.upper()
#             out.append(letter)
#             i+=1
#         else:
#             letter.lower()
#             out.append(letter)
#     return out
# result=myfunc('helloworld')
# print(result)

def myfunc(x):
    out = []
    for i in range(len(x)):
        print(i)
        if i%2==0:
            out.append(x[i].upper())
        else:
            out.append(x[i].lower())
    return ''.join(out)
result=myfunc('Anthropomorphism')
print(result)

# Function Exeercise Level 1
#LESSER OF TWO EVENS: Write a function that
# returns the lesser of two given numbers if both numbers are even, 
# but returns the greater if one or both numbers are odd
def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    elif a%2==0 or b%2==0:
        return max(a,b)
    else:
        return max(a,b)
result=lesser_of_two_evens(5,1)
print(result)

def first_letter(word1,word2):
    if word1[0] == word2[0]:
        return True
    else:
        return False
a=first_letter('Malik','Ali')
print(a)

def is_20(a,b):
    if a+b==20:
        return True
    elif a==20 or b==20:
        return True
    else:
        return False
result=is_20(220,-200)
print(result)

def capatilize(name):
    out=[]
    for i in range(len(name)):
        if i==0:
            out.append(name[i].upper())
        elif i==3:
            out.append(name[i].upper())
        else:
            out.append(name[i].lower())
    return ''.join(out)
x=capatilize('macdonald')
print(x)         

def is_reversed(sentence):
    words=sentence.split()
    reversed_words=words[::-1]
    return ' '.join(reversed_words)
result=is_reversed('I am a programmer')
print(result)

def is_num(n):
    if n<=110 and n>=90:
        return True
    elif n<=210 and n>=190:
        return True
    else:
        return False
result=is_num(205)
print(result)

def has_33(arr):   
    for num in range(len(arr)):
        
        if arr[num]==3 and arr[num+1]==3:
            
            return True
            num+=1
    
    return False
res=has_33([1,3,4,8,3,3])
print(res)

def lets_repeat(word):
    out=[]
    for letter in word:
        out.append(letter*3)
    return ''.join(out)
result=lets_repeat('Hello')
print(result)        
    
def myfunc(a,b,c):
    if a+b+c<=21:
        return a+b+c
    elif a==11 or b==11 or c==11:
        a+b+c-10>=21    
        sum= a+b+c-10
        return sum
    elif a+b+c>21:
        return 'Blast'
        
    
result=myfunc(10,10,10)
print(result)

# def sum_(*args):
#     for num in args:
#         if args[num]<6 and args[num]>9:
#             return sum(num)
# result=sum_(1,2,3,6,9,10)
# print(result)

def game(mylist):
    out=[]
    for i in range(len(mylist)):
        print(i)
        if i==0:
            out.append(i)
        elif i+1==0:
            out.append(i)
        elif i+2==7:
            out.append(i)
        return True
    else:
        return False

    
result=game([1,3,1,8,1,2,0,7])
print(result)
# numbers =list(range(1,50))
# print(numbers)
def myfunc(numbers):
    out=[]
    for num in numbers:
        if numbers[num]%num==0:
            print(numbers)
            print(num)
            out.append(numbers)
        return out
        
        
result=myfunc(list(range(1,50)))
print(result)  

def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        
        for y in range(3,x,2):  # test all odd factors up to x-1
            print(num)
            print('x:',x)
            print('y:',y)
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
result=count_primes(20)
print(result)
    
                 