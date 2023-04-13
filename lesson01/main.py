from tkinter import Tk


# Объект - единица информации в памяти
# Экземпляр - конкретный объект какого-то класса
# Класс - инструкции по созданию объектов определённого типа
# Метод - функция в классе для воздействия на объект
# поля или свойства - переменные в классе
# атрибуты - все имена в классе: переменных и методов

# root = Tk()
# root.mainloop()

# class Purse:
#     def show(team_side, name='Unknown'):
#         print("hello " + name)
#
# x = Purse()
# # print(type(x))
# y = Purse()
# x.show()
# y.show('Alise')


class Purse:
    def __init__(self, currency, name='Unknown'):
        if currency not in ('USD', 'EUR'):
            raise ValueError
        # инкапсуляция - защита данных __money - доступ только из классов
        # С _money можно получить доступ через _money
        self.__money = 0.00
        self.currency = currency
        self.name = name

    def top_up_balance(self, how_many):
        self.__money += how_many
        return how_many

    def top_down_balance(self, how_many):
        if self.__money - how_many < 0:
            # print('Недостаточно средств')
            raise ValueError('Недостаточно средств')
        self.__money = self.__money - how_many
        return how_many

    def info(self):
        print(self.name, self.__money, self.currency)

    def __del__(self):
        print('Кошелёк удалён')


x = Purse('USD')
y = Purse('USD', 'Alexey')
y.top_up_balance(100)
x.info()
y.info()
x.top_up_balance(y.top_down_balance(7))
# x.money = -200  # доступа нет
x.info()
y.info()
# x.top_down_balance(200)
# del x
