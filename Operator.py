# Input, range, enumerator, shuffle, randint, etc
for number in range(1,100,5):
    print(number)

for mylist in range(1,20):
    print(mylist)

mylist1=[1,2,3,4]
mylist2=['a','b','c']
mylist3=[100,200,300]
combine= list(zip(mylist1, mylist2,mylist3))
print(combine)

from random import randint
a=randint(1,100)
print(a)