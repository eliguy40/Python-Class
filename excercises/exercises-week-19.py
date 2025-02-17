
fruits = ["Apples", "Oranges", "Grapefruit"]

vegetables = ["Broccoli", "Cabbage", "Lettuce", "Bell Peppers"]

shopping_list = [["Milk", "Soda", "O.J."], ["Honey Bunches of Oats", "Granola", "Life"]]

shopping_list.append(vegetables)

shopping_list.append(fruits)

print(shopping_list[1]) # Cereal print

# Replace Honey Bunches of Oats with Wheaties
old_cereal = "Honey Bunches of Oats"
new_cereal = "Wheaties"

for word in range(len(shopping_list)):
    for nest_word in range(len(shopping_list[word])):
        if shopping_list[word][nest_word] == old_cereal:
            shopping_list[word][nest_word] = new_cereal

print(shopping_list) # Print change
# Adds grapes to fruits
shopping_list[3].append("Grapes")

print(shopping_list[3])
# Adds multiple drinks to drink list
shopping_list[0].extend(["Sprite", "Mountain Dew", "Grapefruit Juice", "Sparkling Water", "Kombucha"])

print(shopping_list[0])
# Combines fruits and vegetables list
shopping_list = shopping_list[0], shopping_list[1], shopping_list[2] + shopping_list[3]

print(shopping_list)
# Multiplies cereal list by 3
shopping_list = shopping_list[0], shopping_list[1] * 3, shopping_list[2]

print(shopping_list)
# Prints 4 and 5 in fruits and vegetables list
print(f"{shopping_list[2][4]}, {shopping_list[2][5]}")

