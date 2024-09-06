class House:

    houses_history = []

    def __new__ (cls, *args, **kwargs):
        House.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__ (self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to (self, new_floor):
        print('\n', self.name)
        if int(new_floor) >= 1 and new_floor <= self.number_of_floor:
            print('Вы можете поехать на эти этажи:')
            for i in range(1, self.number_of_floor):
                print (i, end =', ')
            print(self.number_of_floor)
        else:
            print ('Такого этажа не существует')

    def __len__ (self):
        return self.number_of_floor

    def __str__ (self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floor}')

    def __eq__ (self, other):
        return self.number_of_floor == other.number_of_floor

    def __lt__ (self, other):
        return self.number_of_floor < other.number_of_floor

    def __le__ (self, other):
        return self.number_of_floor <= other.number_of_floor

    def __gt__ (self, other):
        return self.number_of_floor > other.number_of_floor

    def __ge__ (self, other):
        return self.number_of_floor >= other.number_of_floor

    def __ne__ (self, other):
        return self.number_of_floor != other.number_of_floor

    def __add__(self, value):
        self.number_of_floor = self.number_of_floor + value
        return House(self.name, self.number_of_floor)

    def __radd__ (self, value):
        self.number_of_floor = value + self.number_of_floor
        return House(self.name, self.number_of_floor)

    def __iadd__ (self, value):
        self.number_of_floor += value
        return House(self.name, self.number_of_floor)

    def __del__ (self):
        print(f'{self.name} снесён, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)