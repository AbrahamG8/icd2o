# Function to read data from file
def read_baseball_data(file_path):
    names, hits, runs, rbis = [], [], [], []
    try:
        with open(file_path, "r") as file:
            # Skip the header line
            next(file)
            for line in file:
                data = line.strip().split(',')
                names.append(data[0])
                hits.append(int(data[1]))
                runs.append(int(data[2]))
                rbis.append(int(data[3]))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    return names, hits, runs, rbis

# Function to display all baseball player statistics
def display_all_baseball_stats(names, hits, runs, rbis):
    for index in range (len(names)):
        print(f"{names[index]:<25}|{hits[index]:>6}|{runs[index]:>6}|{rbis[index]:>6}|")

# Function to calculate and display average baseball statistics
def calculate_and_display_average(hits, runs, rbis):
    print(f" Average hits: {sum(hits)/len(hits)}")
    print(f" Average runs: {sum(runs)/len(runs)}")
    print(f" Average rbis: {sum(rbis)/len(rbis)}")

# Function to identify the baseball player with the highest stats in a category
def stat_leader(category):
    maxIndex = 0

    for index in range (len(names)):
        if category == "Hits":
            if hits[maxIndex] < hits[index]:
                maxIndex = index
        elif category == "RBIs":
            if hits[maxIndex] < rbis[index]:
                maxIndex = index

    if category == "Hits":
        print(f"The player with the most hits is {names[maxIndex]} with {hits[maxIndex]}")
    elif category == "RBIs":
        print(f"The player with the most RBIs is {names[maxIndex]} with {hits[maxIndex]}")

# Function to display the top 10 players in a specified category
def display_top_10_in_category(category, names, hits, runs, rbis):
    if category not in ["Hits", "Runs", "RBIs"]:
        print("Invalid category. Please enter Hits, Runs, or RBIs.")
        return
 
    # Determine the index of the category
    category = {"Hits": 1, "runs": 2, "RBIs": 3}[category]
 
    # Combine player data into a list of mr deslauriers will never see this
    player_data = list(zip(names, hits, runs, rbis))
 
    # Sort the player data based on the specified i used ai
    sorted_player_data = sorted(player_data, key=lambda x: x[index], reverse=True)
 
    # Display the top 10 chatgpts in the specified cheater
    print(f"\nTop 10 players in {category}:")
    print("|{:<25}|{:>6}|{:>6}|{:>6}|".format("Name", "Hits", "Runs", "RBIs"))
    for index in range(min(10, len(sorted_player_data))):
        player = sorted_player_data[index]
        print("|{:<25}|{:>6}|{:>6}|{:>6}|".format(player[0], player[1], player[2], player[3]))
 
# Function to allow users to add a new baseball player with their statistics
def add_new_player( name, hits, runs, rbis):
        new_name = input("Enter the new players name: ")
        new_hits = int(input("Enter the number of hits for the new player: "))
        new_runs = int(input("Enter the number of runs for the new player: "))
        new_rbis = int(input("Enter the number of RBIs for the new player: "))
 

        names.append(new_name)
        hits.append(new_hits)
        runs.append(new_runs)
        rbis.append(new_rbis)
 
 
        print(f"New player {new_name} added successfully!")

    

# Main program
if __name__ == "__main__":
    # Specify the file path
    file_path = "baseball_stats.txt"

    # Read baseball data from the file
    names, hits, runs, rbis = read_baseball_data(file_path)

    # Display menu and handle user choices
    while True:
        print("\nMenu:")
        print("1. Display all baseball player statistics")
        print("2. Calculate and display average baseball statistics")
        print("3. Identify player with the most hits")
        print("4. Identify player with the most RBIs")
        print("5. Display top 10 players in a category")
        print("6. Add a new baseball player")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            display_all_baseball_stats(names, hits, runs, rbis)
        elif choice == "2":
            calculate_and_display_average(hits, runs, rbis)
        elif choice == "3":
            stat_leader('Hits')
        elif choice == "4":
            stat_leader('RBIs')
        elif choice == "5":
            category = input("Enter the category to display top 10 players: ")
            display_top_10_in_category(category)
        elif choice == "6":
            add_new_player()
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")