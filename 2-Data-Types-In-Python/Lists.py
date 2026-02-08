# Lists are mutable
ingredients = [
    "Water",
    "Milk",
    "Black Tea",
    "Sugar"
]

print(ingredients)
ingredients.remove("Water")

print(ingredients)


spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

print(chai_ingredients)
print(spice_options)

chai_ingredients.extend(spice_options)
print(chai_ingredients)

chai_ingredients.insert(2, "Black Tea")
print(chai_ingredients)

last_added = chai_ingredients.pop()
print(last_added)
print(chai_ingredients)


chai_ingredients.reverse()
print(chai_ingredients)
