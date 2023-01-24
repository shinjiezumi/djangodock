class A:
    def __init__(self):
        self._number = 10  # プライベート属性には、'_'を付ける慣習がある
        self.__number = 20  # `__`とすると参照できなくはなるが、これは名前の衝突を防ぐため。参照する方法はある。


a = A()
print(a._number)  # ルール的なものでエラーにはならない。

# print(a.__number)  # エラー
print(a._A__number)  # 無理やり参照することもできる。


# 名前の衝突を防ぐために'__'を使う
class A:
    def __init__(self):
        self.__value = 1


class B(A):
    def __init__(self, name):
        super().__init__()
        self.name = name


class C(B):
    def __init__(self, name):
        super().__init__(name)
        self.value = 10


c = C('hoge')
print(c.value)
