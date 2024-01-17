#1
n = 0
while (n <= 0):#while is not positive
    n = int(input("Please enter a positive number:"))

#2
import random
n = random.randInt(1,10)

guess = 0
while guess != n :
    guess = int(input('Enter your guess: '))
    if guess < n :
        print('Too low')
    elif guess > n:
        print('Too high')
    else:
        print('correct')

#3
n = 2
sum = 0
while n <= 10:
    sum += n
    n += 2 

print(sum)