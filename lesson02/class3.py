class A:
    def a(self):
        print('A')


class B:
    def a(self):
        print('B')


class C(B):
    def a(self):
        print('C')


class D(C, A):

    def a(self):
        super(B, self).a()
        # super().a()
        # print(team_side.__class__.__mro__)


D().a()
# __mro__ выводит порядок поиска методов в родителях
# print(D.__mro__)


class Verification:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__lenpassword()

    def __lenpassword(self):
        if len(self.password) < 8:
            raise ValueError('слабый пароль')

    def save(self):
        with open('users', 'a') as r:
            r.write(f'{self.login, self.password}\n')
