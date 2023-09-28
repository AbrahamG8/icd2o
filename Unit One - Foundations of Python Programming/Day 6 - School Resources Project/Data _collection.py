print("Welcome to the school data Resources assesment Program!")

print("**Location: Bayviewglen**")
      
print("**Data Collection**")  

print("1. Total Washrooms")

total_washrooms = str(input("Please enter the total amount of washrooms here:")) 
location_of_washrooms = str(input("Please enter the locations of the water fountains:(seperated by commas)"))
cleanliness_of_washrooms = str(input("Please describe the cleanliness of washrooms:"))


print("2. Total classrooms")
total_classrooms = str(input("Please enter the total amount of classrooms here: "))

print("3. Total fountains")
total_fountains = str(input(" Please enter the total amount of fountains:"))
location_of_fountains = str(input("Please enter the locations of the fountains: (seperated by commas)"))
describe_the_condition_of_fountains = str(input("Please describe the condition of the fountains"))

print("**Data Collected**")

print(f"total washrooms collected " + {total_washrooms})
print(f"location of washrooms" + {location_of_washrooms})
print(f"cleanliness" + {cleanliness_of_washrooms})

print(f"total number of classrooms" + {total_classrooms})

print(f"total fountains collected" + {total_fountains})
print(f"locations" + (location_of_fountains))
print(f"conditions" + {describe_the_condition_of_fountains})