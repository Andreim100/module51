# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.say_info()
#         self.birthday()
#     def say_info(self):
#         print(f"Здрасьте, я {self.name} и мне {self.age} лет")
#
#     def birthday(self):
#         self.age+= 1
#         print(f'У меня день рождения, мне теперь {self.age} лет')
#
# den = Human('Денис',23)
# max = Human('Максимка',44)


# max.birthday()
# den.say_info()
# max.say_info()
# print(den.name, den.age)
# den.surname = 'Фролов'
# print(den.surname)
# print(max.name, max.age)

class House :
    def __init__(self, name, number_of_floors,num):
        self.name = name
        self.numbers_of_floors = number_of_floors
        self.info()
        self.go_to()
    def info (self):
        print(f"Жилой класс {self.name} и у меня {self.numbers_of_floors} этажей'")
    def go_to(self):
        for i in range(num):
            print(f'этажей {self.i}')
gor = House('ЖК Горский',18,5)
domik = House ('Домик в деревне',2,7)
