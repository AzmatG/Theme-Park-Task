class Attraction:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def get_name(self):
        return self.name

    def get_capacity(self):
        return self.capacity

    def get_details(self):
        return f"Attraction name: {self.name}\nAttraction Capacity: {self.capacity}"

    def start(self):
        return f"{self.name} is now starting! Buckle up!"
            