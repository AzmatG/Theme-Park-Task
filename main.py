from base import Attraction

class Thrillride(Attraction):
    def __init__(self, name, capacity, min_height):
        super().__init__(name, capacity)
        self.__min_height = int(min_height)

    def start(self):
        print(f"Thrill ride {self.name} is now starting. Hold on tight!")

    def is_eligible(self, height):
        if height >= self.__min_height:
            return True
        else:
            print("You cannot go on this thrill ride for safety regulations.")
            return False


class FamilyRide(Attraction):
    def __init__(self, name, capacity, min_age):
        super().__init__(name, capacity)
        self.__min_age = int(min_age)

    def start(self):
        print(f"Family Ride {self.name} is now starting. Have lots of fun!")

    def is_eligible(self, age):
        if age >= self.__min_age:
            return True
        else:
            print("For safety regulations, you are not permitted to enter.")
            return False


class Staff:
    def __init__(self, name, role):
        self.__name = name
        self.__role = role

    def work(self):
        print(f"Staff {self.__name} is performing their role: {self.__role}")


class Visitor:
    def __init__(self, name, age, height):
        self.__name = name
        self._age = int(age)
        self._height = int(height)

    
    def name(self):
        return self.__name

    def get_age(self):
        return self._age

    def get_height(self):
        return self._height

    def ride(self, attraction):
        if isinstance(attraction, Thrillride):
            if attraction.is_eligible(self._height):
                attraction.start()
                print(f"I hope {self.__name} has fun!")
            else:
                print(f"{self.__name} is not eligible for the thrill ride.")
        elif isinstance(attraction, FamilyRide):
            if attraction.is_eligible(self._age):
                attraction.start()
                print(f"I hope {self.__name} has fun!")
            else:
                print(f"{self.__name} is not eligible for the family ride.")
        else:
            print("This is not a valid attraction!")



familyride = FamilyRide("Merry_Go_Round", 10, 5)
thrillride = Thrillride("Draconic", 20, 150)
visitor = Visitor("Aizen", 5, 145)
staff = Staff("Bane", "Cleaner")
visitor.ride(familyride)
print(visitor.get_age())