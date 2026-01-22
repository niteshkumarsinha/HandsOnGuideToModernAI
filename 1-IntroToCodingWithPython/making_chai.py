def make_chai():
    print("Starting to make chai")
    if not kettle_has_water():
        fill_kettle()
    plug_in_kettle() 
    boil_water()    
    if not cup_is_clean():
        clean_cup() 
    add_to_cup("tea leaves")
    add_to_cup("milk")
    add_to_cup("sugar") 
    pour_boiled_water_into_cup()
    stir("cup")
    serve("chai")

def serve(beverage):
    print(f"Serving the {beverage}")

def stir(item):
    print(f"Stirring the {item}")

def pour_boiled_water_into_cup():
    print("Pouring boiled water into the cup")
    print("Chai is ready to be served!")


def add_to_cup(ingredient):
    return print(f"Adding {ingredient} to the cup")


def cup_is_clean():
    # Placeholder function to check if the cup is clean
    return False

def clean_cup():
    print("Cleaning the cup")
    print("Cup is now clean")

def plug_in_kettle():
    print("Plugging in the kettle")
    print("Kettle is now plugged in")

def boil_water():
    print("Boiling water")
    print("Water is now boiled")


def kettle_has_water():
    # Placeholder function to check if the kettle has water
    return False

def fill_kettle():
    print("Filling the kettle with water")
    print("Kettle is now filled with water")


make_chai()