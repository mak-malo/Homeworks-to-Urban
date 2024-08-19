class House():
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        print('\n', self.name)
        if int(new_floor) >= 1 and new_floor <= self.number_of_floor:
            print('Вы можете поехать на эти этажи:')
            for i in range(1, self.number_of_floor):
                print (i, end = ', ')
            print(self.number_of_floor)
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floor}')

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
