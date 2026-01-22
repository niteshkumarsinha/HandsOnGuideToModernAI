from chai import Chai, MilkType

class ChaiMaker:
    def make_chai(self, sweetness_level=5, milk_type=MilkType.WHOLE):
        print("Starting to make chai")
        if not self.kettle_has_water():
            self.fill_kettle()
        self.plug_in_kettle() 
        self.boil_water()    
        if not self.cup_is_clean():
            self.clean_cup() 
        self.add_to_cup("tea leaves")
        self.add_to_cup("milk")
        self.add_to_cup("sugar") 
        self.pour_boiled_water_into_cup()
        self.stir("cup")
        chai = Chai(sweetness_level, milk_type)
        chai.describe()
        self.serve("chai")

    def serve(self, beverage):
        print(f"Serving the {beverage}")

    def stir(self, item):
        print(f"Stirring the {item}")

    def pour_boiled_water_into_cup(self):
        print("Pouring boiled water into the cup")
        print("Chai is ready to be served!")


    def add_to_cup(self, ingredient):
        return print(f"Adding {ingredient} to the cup")


    def cup_is_clean(self):
        # Placeholder function to check if the cup is clean
        return False

    def clean_cup(self):
        print("Cleaning the cup")
        print("Cup is now clean")

    def plug_in_kettle(self):
        print("Plugging in the kettle")
        print("Kettle is now plugged in")

    def boil_water(self):
        print("Boiling water")
        print("Water is now boiled")


    def kettle_has_water(self):
        # Placeholder function to check if the kettle has water
        return False

    def fill_kettle(self):
        print("Filling the kettle with water")
        print("Kettle is now filled with water")


chai_maker = ChaiMaker()
chai_maker.make_chai()