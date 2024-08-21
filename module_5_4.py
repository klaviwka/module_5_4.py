class House:
    houses_history = []

    def __init__(self, name, height):
        self.name = name
        self.height = height
        House.houses_history.append(self.name)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")
        House.houses_history.remove(self.name)

    def new(self, name, height):
        return House(name, height)

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
del h2
del h3

print(House.houses_history)
