from class3 import Verification


# Наследование
class V2(Verification):

    def __init__(self, login, password, age):
        # super() Автоматически ищет методв в родительских классах
        super().__init__(login, password)
        # Verification.__init__(team_side, login, password)
        self.__save()
        self.age = age

    def __save(self):
        with open('users') as r:
            for i in r:
                if f'{self.login, self.password}\n' == i:
                    raise ValueError('Такой есть')
        super().save()
        # Verification.save(team_side)

    def show(self):
        return self.login, self.password


x = V2("Bob", "123456789", 24)
# print(x.show())
