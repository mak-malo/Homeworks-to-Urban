"""Developer - не отлько разработчик"""
class House():
    def __init__(self, name, number_of_floar):
        self.name = name
        self.number_of_floar = number_of_floar

    def go_to(self, new_floar):
        print('\n', self.name)
        if int(new_floar) >= 1 and new_floar <= self.number_of_floar:
            print('Вы можете поехать на эти этажи:')
            for i in range(1, self.number_of_floar):
                print (i, end = ', ')
            print(self.number_of_floar)
        else:
            print('Такого этажа не существует')

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)