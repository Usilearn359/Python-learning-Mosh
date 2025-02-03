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