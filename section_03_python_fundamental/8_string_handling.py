# Basic string handling
# char string ->  alphanumeric data (characker + number data)

email = "nudan.akman1234@gmail.com" # double quotes
name = 'nurdan akman' # single quotes
data = """     
        line1
        line2
        line3
        """   #like paragraph, or multi line triple quotes

print(data)

# String operations
a = "hi"
b = "it's me"
marks = 78

c = a + " " + b # concatenation
print(name*3) # multiplication
print("mark is : " + str(marks)) # tyoe casting


#fetch substrings
data = "  nurdaN is here IS  "

print(data[0]) #single char fetch
print(data[2:8]) # some part fetch
print(data[2:]) #fetch with only starting index
print(data[:9]) #fetch with only end index
print(data[-2]) # single char fetch with negative index 

#string operations
print(len(data)) #length
print(data.upper()) # convert upper case
print(data.lower()) # convert lower case
print(data.capitalize()) # convert first char to upper case, convert others to lower case
print(data.lstrip()) #delete space from left
print(data.rstrip()) #delete space from right
print(data.strip()) #remove space from left & right
print(data.rsplit()) # convert string to the list

#advance string operations
print(data.replace("is", "##")) #replace some part
print(data.replace("is", "§§§").replace("IS","$$$")) #replace two substring in one string
print(data.find("is")) #find data in string
print(data.find("agile")) #find but is not exist -> -1 mean is not exist

print(data.split(" ")) # split based on space and create a list

#string comparison
a = "   Hello"
b = "Hello   "
c = "Hello"
d = "hello"

#case sensitive
if(a.strip() == b.strip()):
    print("same")
else:
    print("not same")

#case insensitive
if(c.upper() == d.upper()): #or lower
    print("same")
else:
    print("not same")
