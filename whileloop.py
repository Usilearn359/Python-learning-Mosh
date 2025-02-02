# Practice while loop
x=0


while x<5:
    x=x+1
    if x<5:
        print(f'x is: {x}')
    else:
        print("X is no longer less than 5")
y=0
while y<5:
    y=y+1
    print(y)

#Continue

name="usmaniqbal"
for letter in name:
    if letter == "a":
        continue
    print(letter)
#pass
x=[1,2,3]
for item in x:
    pass
print("end of my script")
# Break
for letter in name:
    if letter == "b":
        break
    print(letter)
    
    