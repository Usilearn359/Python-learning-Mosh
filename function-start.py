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