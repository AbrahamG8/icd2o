age = 32
name = "Steve"

print("Name:" + name + ". Age:" + str(age))
#works but we need to add + everywhere and we keep opening and closing the brackets
#we have to change everything into a string using str()

#the other option is to use f-strings 
print(f"Name:{name}. Age: {age} years")