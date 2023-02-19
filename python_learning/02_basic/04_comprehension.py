# 内包表記
# 各要素の数値の2乗を求める

# 一般的な書き方
numbers = [1, 5, 6, 11, 3, 5, 7, 3]
squares = []
for num in numbers:
    squares.append(num ** 2)

print(squares)

# 内包表記
squares = [num ** 2 for num in numbers]
print(squares)

# 各文字列を大文字にする
words = ['python', 'go', 'php']
upper_words = [word.upper() for word in words]
print(upper_words)  # ['PYTHON', 'GO', 'PHP']

# 1から10までの偶数を求める
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)

# 二次元配列で九九を求める
table = [[x * y for x in range(1, 10)] for y in range(1, 10)]
print(table)

# set や dictにも使える
sets = {x for x in range(10)}
print(sets)

dicts = {x: "デフォルト値" for x in range(10)}
print(dicts)

# dict のキー、値を逆転する
score = {'math': 80, 'english': 20}
new_score = {value: key for key, value in score.items()}
print(new_score)  # {80: 'math', 20: 'english'}
