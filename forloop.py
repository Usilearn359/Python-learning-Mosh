mylist=[1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print(num)
    print("Hello")

for num in mylist:
    if num%2==0:
        print(f'Even num: {num}')
    else:
        print(f'Odd num: {num}')


list_sum=0
for num in mylist:
    list_sum += num
    print (list_sum)
print(f'list_sum: {list_sum}')

mystring ='Hello World'
for letter in mystring:
    print(letter) 
    
tup=(1,2,3,4,5,6,7,8,9,10)
for num in tup:
    print("nice")
    

tup=[(1,2),(3,4),(5,6),(7,8)]
for items in tup:
    print(items)

tup=[(1,2),(3,4),(5,6),(7,8)]
for a,b in tup:
    print(a,b)
    print(a)
    print(b)
    
d= {'k1':1, 'k2':2, 'k3':3}
for keys, value in d.items():
    print(value)