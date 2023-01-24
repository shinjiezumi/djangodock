def add(a, b):
    return a + b


# 「if __name__ == '__main__':」とすると、calc.pyを直接実行した時だけ有効になる
if __name__ == '__main__':
    result = add(1, 3)
    print(result)
