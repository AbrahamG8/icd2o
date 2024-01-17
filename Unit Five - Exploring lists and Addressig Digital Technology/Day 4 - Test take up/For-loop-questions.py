#1 - for loops
sum = 0
for alex in range (1,21):
    if alex % 2 == 0:
        sum += alex
print(sum)

#2
letter = (input("Please enter a letter: "))
n = int(input("Please enter a number: "))
result = ''
for i in range (n):
    result += letter

print(result)

#3
for monkey in range (8,0,-1):
    print("monkey")

