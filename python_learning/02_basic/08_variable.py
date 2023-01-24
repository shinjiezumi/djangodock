num = 1


def test():
    global num  # 関数内でグローバル変数を指定することが可能
    num = 100
    print(num)


print(num)
test()
print(num)
