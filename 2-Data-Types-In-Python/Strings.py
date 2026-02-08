# Strings

chai_type = "Green Tea"
print("Chai type:", chai_type)


customer_name = "Alice"
print("Customer name:", customer_name)


print("Order for {}: {}".format(customer_name, chai_type))


chai_description = "A refreshing blend of green tea leaves and herbs."
print(chai_description[0])  # First character
print(chai_description[-1])  # Last character
print(chai_description[0:5])  # First 5 characters
print(chai_description[5:])  # From 5th character to end
print(chai_description[:5])  # First 5 characters

print(chai_description.split())  # Split into words
print(f"First word: {chai_description.split()[0]}")
print(f"First 8 characters: {chai_description[:8]}")

print(chai_description.upper())  # Uppercase
print(chai_description.lower())  # Lowercase
print(chai_description.replace("green", "black"))  # Replace substring
print(chai_description[::-1])  # Reverse string

print("Is 'green' in description?", "green" in chai_description)


label_text = "Chai Special"
print(label_text.center(20, "*"))  # Center with padding
print(label_text)
print(label_text.encode("utf-8"))

encoded_label = label_text.encode("utf-8")
decoded_label = encoded_label.decode("utf-8")
print(decoded_label)




