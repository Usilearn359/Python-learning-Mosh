# statement assesment test
#Task 1 Use for, .split(), and if to create a Statement that will print out words that start with 's':
st='print only the words that start with s in the sentence'
index=0
a=st.split()
print(a)
for word in a:
    if word[0]=='s':
        print(word)
        
        
    #task 2 Use range() to print all the even numbers from 0 to 10.


    
mylist=list(range(0,11,2))
print(mylist)
mylist=[]
for num in range(0,11):
    if num%2==0:
        mylist.append(num)
print(mylist)

#task 3Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.


number=[]
for num in range(1,50):
    if num%3==0:
       number.append(num) 
print(number)

#task 4 Go through the string below and if the length of a word is even print "even!"
st='print only the words that start with s in the sentence'
a= st.split()
print(a)
for word in a:
    if len(word)%2==0:
        print('Even')
    else:
        print('Odd')

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for num in range(1,101):
    print(num)
    if num%3==0 and num%5==0:
        print('FizzBuzz')
    elif num%5==0:
        print('Buzz')
    elif num%3==0 :
        print('Fizz')
    else:
        print('Not a multiple of both')   
        
    #Task 6 Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
a=st.split()
mylist=[]
for word in a:
    mylist.append(word[0])
print(mylist)
 # Great Job!