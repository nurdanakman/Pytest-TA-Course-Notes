# array = list but list take any data type

#define a list
programming_languages = [2021, "python", False, "a"]
programming_languages_latest = [12, "trial"]

print(programming_languages) #display all data of list
print(len(programming_languages)) # lenght
print(programming_languages[3]) # fetch via index
print(programming_languages[0:2])
print(programming_languages[1:])

# 1 approach
for i in range(0, len(programming_languages)):
    print(programming_languages[i])
# 2 approach
for data in programming_languages:
    print(data)


# List operations (read & write)

#concatination
final_list = programming_languages + programming_languages_latest
print(final_list)
#write operation
programming_languages[3] = "somethings"
print(programming_languages)
#insert value
programming_languages.insert(2, "PHP")
print(programming_languages)
#remove an index
programming_languages.remove("somethings")
print(programming_languages)
#add an index
programming_languages.append("somethings_new")
print(programming_languages)

