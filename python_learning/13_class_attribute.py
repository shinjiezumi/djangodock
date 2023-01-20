class A:
    def __init__(self):
        self.number = 10  # インスタンス属性


class B:
    number = 10  # クラス属性


# インスタンス属性
a = A()
print(a.number)

b = B()
print(b.number)

# クラス属性
print(B.number)

print(A.number)  # AttributeError: type object 'A' has no attribute 'number'
