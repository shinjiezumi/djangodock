class A:
    def __init__(self):  # __xx__を特殊メソッドという
        self.count = 1

    def __len__(self):
        return 10

    def __iter__(self):
        return self

    def __next__(self):
        current = self.count
        if current > 10:
            raise StopIteration
        self.count += 1
        return current

    def __getitem__(self, item):
        return item

    def __str__(self):
        return 'Aクラスです'


a = A()
print(len(a))  # 10

for count in a:  # インスタンスをfor文に指定すると、iter,nextが呼び出される
    print(count)

print(a[0])  # getitemが呼び出される

print(a)  # strが呼び出される
