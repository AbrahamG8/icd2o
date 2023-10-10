name = str(input("Enter your name:"))
Opponent_name1 = "Alex"
Opponent_name2 = "Ishaan"
Opponent_name3 = "Arees"
Opponent_name4 = "Brandon"
Opponent_name5 = "Keaton"

your_total = int(input("Enter total here: "))
opponents_total = int(input("Enter opponents total here: "))
overall = your_total + opponents_total
game_one = int(input("Input your game one points here: "))
game_two = int(input("Input your game two points here: "))
game_three = int(input("Input your game three points here: "))
game_four = int(input("Input your game four points here: "))
game_five = int(input("Input your game five points here"))

opponent_r_five = int(input("Input opponents game five points here"))
opponent_r_four = int(input("Input opponents game four points here: "))
opponent_r_three = int(input("Input opponents game three points here: "))
opponent_r_two = int(input("Input opponents game two points here: "))
opponent_r_one = int(input("Input opponents game one points here: "))

box_percentage1 = int(game_one/36)
box_percentage2 = int(game_two/36)
box_percentage3 = int(game_three/36)
box_percentage4 = int(game_four/36)
box_percentage5 = int(game_five/36)

 


print (f"{name}'s results: ")

print("Game #1: ")
print(f"Opponents Name: {Opponent_name1}")
print(f"Your points: {game_one}")
print(f"Opponents Points: {opponent_r_one} ")


print("Game #2: ")
print(f"Opponents Name: {Opponent_name2}")
print(f"Your points: {game_two} ")
print(f"Opponents Points: {opponent_r_two} ")


print("Game #3: ")
print(f"Opponents Name: {Opponent_name3}")
print(f"Your points: {game_three} ")
print(f"Opponents Points: {opponent_r_three} ")


print("Game #4: ")
print(f"Opponents Name: {Opponent_name4}")
print(f"Your points: {game_four} ")
print(f"Opponents Points: {opponent_r_four} ")



print("Game #5: ")
print(f"Opponents Name: {Opponent_name5}")
print(f"Your points: {game_five} ")
print(f"Opponents Points: {opponent_r_five} ")


print("Dots and Boxes Table Tracker:")

print(f"Player Name: {name}")

print("Opponent         Your Points          Opponents Points                    Total ")
print("------------------------------------------------------------------------")
print(f"{Opponent_name1} {game_one:>22} {opponent_r_one:>23} {box_percentage1:>22.2%}")
print(f"{Opponent_name2} {game_two:>22} {opponent_r_two:<23} {box_percentage2:>19.2%}")
print(f"{Opponent_name3} {game_three:>22} {opponent_r_three:>19} {box_percentage3:>16.2%}")
print(f"{Opponent_name4} {game_four:>22} {opponent_r_four:>21} {box_percentage4:>22.2%}")
print(f"{Opponent_name5} {game_five:>22} {opponent_r_five:>16} {box_percentage5:>22.2%}")
print("------------------------------------------------------------------------")


print("Summary: ")
print(f"Your Total Points: {your_total}")
print(f"Total Opponent Points: {opponents_total}")
print(f"Total Points: {overall}")