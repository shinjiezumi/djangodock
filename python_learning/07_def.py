# def
def hello(name):
    message = '{0}sさん、こんにちは'.format(name)
    print(message)


hello('hoge')


# デフォルト引数
def hello2(name='匿名'):
    print(name)


hello2()


# 必須引数は先に定義する
def hello3(text, name='匿名'):
    print(text, name)


## text をキーワード引数という
hello3(text='こんにちは')
hello3(text='こんにちは', name='太郎')

## 省略した引数を位置引数という
hello3('こんにちは', '太郎')


# 任意の数の引数を受け取る.
# '*'１つで位置引数をまとめることができる
# 引数名は'args'とするのが慣習
def hello4(*args):
    print(args)


hello4('hoge', 'fuga')


# '*'２つでキーワード引数をまとめることができる
# 引数名は'kwargs'とするのが慣習
def hello5(*args, **kwargs):
    print(args)  # ('hoge', 'fuga')
    print(kwargs)  # {'a': 1, 'b': 2, 'c': 3}


hello5('hoge', 'fuga', a=1, b=2, c=3)


# '*'を付けるとキーワード専用引数になる。キーワード引数でしか渡せなくなる
def hello6(text, *, name='匿名'):
    print(text, name)


hello6('こんにちは')
hello6('こんにちは', name='太郎')
hello6('こんにちは', '太郎')  # エラー
