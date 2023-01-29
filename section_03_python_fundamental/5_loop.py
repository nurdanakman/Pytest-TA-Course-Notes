#for loop with final value (range)
# default value = 0
for i in range(10):
    print(i)

final_number = input("enter an number: -")
final_number = int(final_number)
for i in range(final_number):
    print(i)

print("---------------------------------")

#for loop with start and end value
z = 5
for i in range(3,13):
    print(str(z) + " * " + str(i) +" = " + str(z*i))

print("---------------------------------")

#for loop increment / decrement
for i in range(1,11,2):
    print(i)

print("---------------------------------")

for i in range(11,1,-3):
    print(i)

print("---------------------------------")

#for loop with list
li = [1,2,3,4,5,6,7,8,9,"string","c",.6]
for i in li:
    print(i)

print("---------------------------------")

#string is a char list
for i in "nurdan akman":
    print(i)

print("---------------------------------")

#sum function
li =[4,6,78,90,24,85]
sum=0
for i in li:
    sum = sum + i
print(sum)

print("---------------------------------")

#while loop