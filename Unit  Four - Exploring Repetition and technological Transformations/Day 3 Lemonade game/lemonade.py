# get the weather function - the function will have a list and return a random choice (like hangman)

# get player input (how many cups of lemonade, adevertising signs, price per cup) 
# the first 2 we are spending $$, argument pass in the assetts (how much $$ you have)
# make sure they have the $$ to make the lemonade and  buy the signs
# update the assetts after you spend the $$

#counter for the day

# display the recap for the day
# how many you sold, how much you made (+ or -), current assests

import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')



customers = random.randint(5,10)

print(customers)

weather = ["cold and sunny","hot and sunny","rainy"]
weather_multiplier = [2, 5, 0.2]

weather_type = random.randint(0,2)  # random number 0, 1 or 2

print(weather_type)     # print to see it
cls()
weath = weather[weather_type]
multiplier = weather_multiplier[weather_type]

print(weath)    # get the weather from the list with that index
print(multiplier) # get the weather from the list with that index

customers *= multiplier

print(customers)



# display instructions

#ask if they want to play again

#while(not gameover):
    # play 1 day of the game
    # ask if they want to play again
    # if no gameover = True






cups_lemonade = int(input("How much cups of lemonade do you want to make?:"))
advertising_signs = int(input("How many advertising signs do you want to make?:"))
sell_price = int(input("How much do you wanto to sell each lemonade cup for (in cents)?:"))

def intro_to_lemonade(cups_lemonade, advertising_signs, sell_price):
    print("Hi, welcome to Great Yorkleybergh. In this small town you are in charge of a lemonade stand and all of it's costs. You will need to make 3 decisions daily: how many cups you make, how many advertising signs to make, and what price to set the lemonade at")
    print("The profits are the difference between the income and your expenses")
    print("Keep track of your assets so that you don't spend more than you have")
