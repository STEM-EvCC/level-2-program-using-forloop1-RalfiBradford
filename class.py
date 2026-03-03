# Basic for loop
# A for loop is used for iterating over a set or range of values
grocery_list = ["eggs", "milk", "pizza", "cereal"]
# for each item x in the list, print the item
for x in grocery_list:
    print(x)

# printing each letter in a word
for x in "Snorlax":
    print(x)

# We can use break to stop the loop before it loops through all items
for x in grocery_list:
    print(x)
    if x == "pizza":
        break
    #print(x) <-- can be used here to not print pizza from the list (make sure to remove it from the if)
print("")
print("")
# we can use continue to stop the current iteration of the loop and continue to the next
for x in grocery_list:
    if x == "pizza":
        continue
    print(x)

# We can use range() to iterate a specific number of times
# Note that range uses index values
for x in range(8):
    print(x)

# we can use the else keyword in conjuction with for loop to execute code when the loop is finished
for x in range(4):
    print(x)
else:
    print("Sequence finished")

# Nested for Loops
spooky_adjectives = ["Frightful", "Scary", "Haunting"]
monster_list = ["Ghost", "Mummy", "Mike Wiczowski"]
for x in spooky_adjectives:
    for y in monster_list:
        print(x,y)

# for loops cannot be empty

# This is wrong for the homework
mission_counter = []