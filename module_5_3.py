class House:
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
        #print(self)

    def __radd__ (self, value):
        self.number_of_floor = value + self.number_of_floor
        return House(self.name, self.number_of_floor)
        #print(self)

    def __iadd__ (self, value):
        self.number_of_floor += value
        return House(self.name, self.number_of_floor)
        #print(self)




h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print('1.', end = '')
print(h1)
print(h2)

print('\n2.', end = '')
print(len(h1))
print(len(h2))

print('\n3.', end = '')
print('h1 =', type(h1), '\nh2 =', type(h2))
print(h1 == h2)

print('\n4.', end = '')
h1 = h1 + 10
print('h1 =', type(h1))
print(h1)
print(h1 == h2)

print('\n5.', end = '')
h1 += 10
print(h1)

print('\n6.', end = '')
h2 = 10 + h2
print(h2)

print('\n7.', end = '')
print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)