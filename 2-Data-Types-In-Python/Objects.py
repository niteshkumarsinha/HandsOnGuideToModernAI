sugar_amount = 10

print(sugar_amount)
print(type(sugar_amount))

print(f"initial sugar: {sugar_amount}")
print(f"ID of sugar_amount: {id(sugar_amount)}")

sugar_amount = sugar_amount + 5
print(f"after adding 5: {sugar_amount}")
print(f"ID of sugar_amount: {id(sugar_amount)}")

sugar_amount += 5
print(f"after adding 5: {sugar_amount}")
print(f"ID of sugar_amount: {id(sugar_amount)}")

print(f"ID of 2: {id(2)}")
print(f"ID of 10: {id(10)}")
print(f"ID of 20: {id(20)}")


spice_mix = set()
print(f"ID of empty set: {id(spice_mix)}")
print(f"Set after adding cardamom {spice_mix}")

spice_mix.add("cardamom")
print(f"ID of set after adding cardamom: {id(spice_mix)}")
print(f"Set after adding cloves {spice_mix}")

spice_mix.add("cloves")
print(f"ID of set after adding cloves: {id(spice_mix)}")
print(f"Set after adding cloves {spice_mix}")