# Define a tuple -> all values can be added -> only read, not write
programming_language = (2021, "python", "java", True, "v")
programming_language_latest = ("b", "trial")
print(programming_language)

print(programming_language[3])
print(programming_language[2:4])
print(programming_language[1:])

print(len(programming_language))

for i in range(0, len(programming_language)):
    print(programming_language[i])

for data in programming_language:
    print(data)

programming_language_final = programming_language + programming_language_latest 
print(programming_language_final)

programming_language[2]="PHP" # you get error, because tuple cannot be changed
