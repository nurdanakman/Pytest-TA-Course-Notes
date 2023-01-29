number = input ("Please enter a number: -")

i = 0
#default
while(i<=10):
    print(i*int(number))
    i = i + 1

print("---------------")

#increment
i = 1
while(i<=10):
    print(i*int(number))
    i +=1  # i = i + 1

print("---------------")

#decrement
i = 10
while(i>=0):
    print(i*int(number))
    i -=1 # i = i - 1

print("---------------")

#break statement -> came out from loop at an condition
for i in range(1,11):
    if(i*int(number) == 30):
        break
    print(i*int(number))

print("---------------")

#continue statement -> skip remaining part of loop
for i in range(1,11):
    if (i*int(number)%10 == 0):
        continue
    print(i*int(number))
