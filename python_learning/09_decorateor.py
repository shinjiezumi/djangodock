# デコレータは既存の関数に別の処理を追加できる
def debug(function):
    def _debug(*args, **kwargs):
        result = function(*args, **kwargs)
        print(function.__name__, args, kwargs, result)
        # 関数の実行結果を返す
        return result

    return _debug


@debug
def say_hello():
    print('hello')


say_hello()


# 簡易
def decorator(function):
    print('decorator')
    return function


def say_hello2():
    print('hello')


say_hello2 = decorator(say_hello2)  # 高階関数
say_hello2()  # decorator \n hello


# 関数の上に[@関数名]とすると代入不要になる
@decorator
def say_hello3():
    print('hello')


say_hello3()  # decorator \n hello
