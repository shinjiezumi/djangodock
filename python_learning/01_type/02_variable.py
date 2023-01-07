a = 1 + 1
print(a)

# 変数名の先頭は_、もしくはアルファベットが使える
_hoge = "hogehoge"
print(_hoge)

# 先頭以外は数字もOK
hoge123___ = 123
print(hoge123___)

# 予約語は使えない
# and = 1

a = 100
b = 200
print(a + b)

# 未定義の変数はエラーになる
# print(c)

# 省略もできる。 a = a + 1の
a += 1
print(a)
