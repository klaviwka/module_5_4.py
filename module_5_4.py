class House:
    houses_history = []

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")
        House.houses_history.remove(self.name)

    def new(self, name, height):
        new_house = House(name, height)
        House.houses_history.append(new_house.name)
        return new_house


house_creator = House('Создатель', 0)

h1 = house_creator.new('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = house_creator.new('ЖК Акация', 20)
print(House.houses_history)
h3 = house_creator.new('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)
