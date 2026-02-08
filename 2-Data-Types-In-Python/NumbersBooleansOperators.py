import sys
from fractions import Fraction
from decimal import Decimal as d

print("Python version:", sys.version)

# Numbers

## Integers
black_tea_grams = 14
ginger_tea_grams = 7

total_tea_grams = black_tea_grams + ginger_tea_grams
print("Total tea grams:", total_tea_grams)

remaoining_tea_grams = total_tea_grams - 5
print("Remaining tea grams after using 5 grams:", remaoining_tea_grams)

milk_litres = 0.5
total_tea_litres = milk_litres + (total_tea_grams / 1000)  
print("Total tea litres:", total_tea_litres)

total_tea_bags = 7
pots = 4
tea_bags_per_pot = total_tea_bags / pots
print("Tea bags per pot:", tea_bags_per_pot)

tea_bags_per_pot = total_tea_bags // pots
print("Tea bags per pot:", tea_bags_per_pot)

total_caramom_pods = 10
pots = 3
pods_per_pot = total_caramom_pods / pots
print("Cardamom pods per pot:", pods_per_pot)


total_caramom_pods = 10
pots = 3
pods_per_pot = total_caramom_pods // pots
print("Cardamom pods per pot:", pods_per_pot)

base_flavor_strength = 2
scale_factor = 3
powerful_flavor_strength = base_flavor_strength ** scale_factor
print("Powerful flavor strength:", powerful_flavor_strength)

total_tea_leaves_harvested = 1_000_000_000
print("Total tea leaves harvested:", total_tea_leaves_harvested)

## Booleans
is_boiling = True
print("Is the water boiling?", is_boiling)
stir_count = 5
print("Is the stir count greater than 3?", stir_count > 3)

total_actions = is_boiling + stir_count
print("Total actions (boiling + stir count):", total_actions)

milk_present = 0
print("Is milk present?", bool(milk_present))




## Real Number (Floats)
ideal_temperature = 95.5
current_temperature = 95.49999999999999999999999999
print("Current temperature:", current_temperature)
print("Ideal temperature:", ideal_temperature)

print("Is the current temperature ideal?", current_temperature == ideal_temperature)
print("Is the current temperature close enough to ideal?", abs(current_temperature - ideal_temperature) < 1e-9)
print("Difference between current and ideal temperature:", current_temperature - ideal_temperature)
print(sys.float_info)

## Complex Numbers
2 + 3j