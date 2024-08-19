"""Developer - не отлько разработчик"""
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

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
