import enum


class MilkType(enum.Enum):
    WHOLE = "whole"
    SKIMMED = "skimmed"
    ALMOND = "almond"
    SOY = "soy"
    OAT = "oat"

class Chai:

    def __init__(self, sweetness_level: int, milk_type: MilkType):
        self.sweetness_level = sweetness_level
        self.milk_type = milk_type


    def sip(self):
        print(f"Sipping the chai with {self.milk_type.value} milk and sweetness level {self.sweetness_level}")

    
    def add_sugar(self, amount: int):
        self.sweetness_level += amount
        print(f"Added {amount} units of sugar. New sweetness level: {self.sweetness_level}")

    def describe(self):
        print(f"This chai has {self.milk_type.value} milk and a sweetness level of {self.sweetness_level}")


if __name__ == "__main__":
    Chai1 = Chai(sweetness_level=5, milk_type=MilkType.ALMOND)
    Chai1.describe()
    Chai1.sip()
    Chai1.add_sugar(2)
    Chai1.sip() 
    Chai1.describe()

    