class Person:
    def __init__(self, name):
        self.name = name

    @property  # self.name のように参照するとこのデコレーターが呼び出される
    def name(self):
        return self._name  # 代入されるのは _nameなので、それを返す

    @name.setter  # nameに代入された際に呼び出される
    def name(self, value):
        if not value:
            value = '名無しの権兵衛'
        self._name = value  # '_'付けないと、本メソッドが呼び出されて無限ループになってしまう。


person = Person('hogehoge')
print(person.name)  # hogehoge

person = Person('')
print(person.name)  # 名無しの権兵衛


# (例)内部向けの名前と外部公開向けの名前を管理
class Person2:
    def __init__(self, name):
        self.origin_name = name
        self.name = name

    @property
    def name(self):
        return self.real_name

    @name.setter
    def name(self, value):
        if not value:
            value = '名無しの権兵衛'
        self.real_name = value


person = Person2('ほげ')
print(person.name)

person2 = Person2('')
print(person2.name)
