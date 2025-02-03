# What is function and why needed
# Print and return

def my_fun():
    print("Hello, World!")
my_fun()

def my_func1(name):
    print(name)
my_func1('Usman')

def my_func2(num1,num2):
    print(num1 + num2)
result=my_func2(10,20)
print(result)

# return
def my_func2(num1,num2):
    return num1 + num2
result=my_func2('10','20')
print(result)
print(type(result))

# check the user guess to find the correct bucket 

from random import shuffle 
def my_list(mylist):
    shuffle(mylist)
    return mylist
result=my_list(['','O',''])
# check the user guess to find the correct bucket
def user_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess=input('pick a number 0,1,2: ')
    return int(guess)
user_guess()

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('correct')
    else:
        print('incorrect')

mylist=['','O','']
mixedup=my_list(mylist)
guess=user_guess()
check_guess(mixedup,guess)

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
