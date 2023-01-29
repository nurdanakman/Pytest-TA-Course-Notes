
data = input("Please enter a number: -")
data = int(data)

#Handle one condition
if( data % 2 == 0 ):
    print("Even")
    print("I am still inside of if condition")
    print("indentation = 1")
print("indentation = 0")

print ("-----------------------")

#Handle 2 conditions
if( data % 2 == 0 ):
    print("Even")
else:
    print("odd")

print ("-----------------------")

#Handle more than two conditions
if( data > 0 ):
    print("positive")
elif (data == 0):
    print("0")
elif(data < 0):
    print("negative")
if( data % 2 == 0 ):
    print("Even")
else:
    print("odd")

print ("-----------------------")

#Nested Conditions
if( data >= 0 ):
    print("positive")
    if( data % 2 == 0 ):
        print("Even")
    else:
        print("odd")
else:
    print("negative")

print ("-----------------------")

#Check multiple conditions OR |
if( data > 100 or data < 0 ):
    print("invalid")
else:
    print("valid")

print ("-----------------------")

#Check multiple conditions AND &
if( (data >= 0) and (data % 2 ==0) ):
    print("even")
elif( (data >= 0) and (data % 2 == 1) ):
    print("odd")
else:
    print("invalid")
