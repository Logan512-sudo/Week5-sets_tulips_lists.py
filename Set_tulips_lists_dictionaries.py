#collections = single "variable" used to store multiple values
# Lists = [] ordered and changable. Duplicates OK
# Set = {} unordered and imutable, but add/remove OK. No duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = {"apple", "Orange", "bannana", "coconut", "Kiwi", "Watermelon"}
#print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)
#print("pineapple" in fruits)

#print(fruits)
#for fruit in fruits:
 #   print(fruit)

#fruits[1] = "pineapple" #reassign values
#fruits.appened("pineapple")
#fruits.remove("apple")
#fruits.insert(0, "pineapple")
#fruits.sort()
#fruits.reverse()
#fruits.clear()

#fruits.remove("apple")
#fruits.add("pineapple")
#fruits.add("strawberry")
#fruits.pop()


#print(fruits[0])

#print(fruits[0])

#for fruit in fruits:
 #  print(fruit)


#cars = ["bmw","mauserati", "audi", "merecedes", "ferrari"]
#print(f"these are list of {cars}")
#print(f"the first car is {cars[0]}")

#changing the value of the list
#cars[0] = "toyota"
#print(f"the first car is {cars[0]}")

#print(f"the last car is {cars[-1]}")
#cars[-1] = "lamborghini"
#print(f"the last car is {cars[-1]}")

#adding a new value to the list
#cars.append("bugatti")
#print(cars)
#cars.remove("maserati")
#print(cars)

#looping through the list
#otherwise called iterating through the list
#for car in cars:
    #pring(len(car))
    #print(car)
    #carRequest = input("add a new car please: ")
    #cars.append(carRequest)
    #print(cars)
    #print.len(cars)
    #print(cars.upper())
    #print(cars)
    #if len(cars) > 10:
     #   break

#Challenge
#Create a list of friends
#make sure the initial list is none

#friends = ["Dexter", "Caiden", "Tony", "Andres", "Robert", "Johny"]

#add a new friends to the list, add at least 5 friends

#friends.append("Mr.Tomczak")
#friends.append("homie number 7")
#friends.append("homie number 8")
#friends.append("homie number 9")
#friends.append("homie number 10")
#print(friends)

#remove a friends
#friends.remove("Mr.Tomczak")
#print(friends)
#insert a friend at a specific index maybe 2
#friends[2] = "The Jackelope from Lunchables"
#print(friends)
#print the list of friends
#for friend in friends:
   # print(len(friends))
#loop through the list and print the friends name
    #print(friend)
    #friendRequest = input("Will you be friends with me? My name is Antonio Olvera and Im lonely, What's your name?")
    #friend.append(friendRequest)
#see if a particular friends is in the list(boolean value)
#if the list is greater than 10 break the loop
   # print(friends)
   # if len(friends) > 10:
    #    break



#DICTIONARIES:

#dictionary = a collection of {key:value} pairs
#             ordered and changeable. No Duplicates

capitals = {"USA": "Washington D.C.",
            "india": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

#print(dir(capitals))
#print(help(capitals))
print(capitals.get("USA"))
print(capitals.get("Japan"))

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

if capitals.get("China"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop("China")
capitals.popitem()
capitals.clear()

keys = capitals.keys()

print(capitals)

for key in capitals.keys():
    print(key)

#values = capitals.values
for value in capitals.values():
    print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")
