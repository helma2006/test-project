class Vehicle:
    def __init__(self, brand, year):   
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Year:  {self.year}")


class Car(Vehicle):
    def __init__(self, brand, year, num_doors):   
        super().__init__(brand, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")


class Motorcycle(Vehicle):
    def __init__(self, brand, year, has_sidecar):   
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar

    def display_info(self):
        super().display_info()
        print(f"Has sidecar:    {self.has_sidecar}")


v = Vehicle("porp", "1999")
c = Car("bmw", "2006", 4)
m = Motorcycle("s200", "2007", "Yes")

v.display_info()
print("--------")
c.display_info()
print("--------")
m.display_info()