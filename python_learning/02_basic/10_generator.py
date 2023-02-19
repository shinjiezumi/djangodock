# 例）1からnまでの二乗した数を返す

# 他言語で一般的な例
def make_squares(n):
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i ** 2)
    return numbers


squares = make_squares(10)
print(squares)


# ジェネレータ関数
# 返す値の前にyieldを付与すると、そのタイミングで値を生成して返す。
# 以下のコードはループのたびに値を作成して返しており、メモリ効率がよい
def make_squares2(n):
    for i in range(1, n + 1):
        yield i ** 2


squares2 = make_squares2(10)
print(squares2)  # <generator object make_squares2 at 0x104c010e0>

for i in squares2:  # 一つずつ値が返すのでループで回す
    print(i)


# 0.1ずつ刻みで指定できるrange関数を作成
def my_range(start, end, step):
    current_number = start
    while current_number < end:
        yield current_number
        current_number += step


for i in my_range(1, 10, 0.1):
    print(i)
