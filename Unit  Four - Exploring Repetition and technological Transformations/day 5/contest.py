#1
# wins = int(input("please enter your amount of wins: "))
# if wins == 5 or 6 :
#     print("group 1")
# elif wins == 3 or 4:
#     print("group 2")
# elif wins == 1 or 2:
#     print("group 3")
# else:
#     wins == 0
#     print("YOU ARE NOW ELIMINATED FROM THE TOURNEY")


#2
sample = input()

row1 = sample.split()
sum = 0 
for i in range (4):
    sum+= int(row1[i])