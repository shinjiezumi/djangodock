# for 変数名 in データの集まり:
#   処理A

names = ['佐藤', '鈴木', '田中']
for name in names:
    print(name)

# tuple や set、文字列も渡せる
my_tuple = (1, 2, 3)
for number in my_tuple:
    print(number)

my_str = 'hello'
for word in my_str:
    print(word)

# dict
band_members = {'ボーカル': '佐藤', 'ギター': '鈴木'}
for part in band_members:  # partにはキー名が入る
    print(part)
    print(band_members[part])

# values で値だけを取り出す
for name in band_members.values():
    print(name)

# items でキーと値を取り出す
for key, value in band_members.items():
    print(key, value)

# アンパック代入
my_tuple = (1, 2)
a, b = my_tuple

items = [
    ['ギター', '鈴木'],
    ['ボーカル', '田中'],
]

for item in items:
    part, name = item
    print('{0}は{1}さんです'.format(part, name))

# 繰り返し数を指定.
# ジェネレーターオブジェクトともいい、一度に配列が作られるわけではなく毎回作成されるので、メモリ効率が良い
for i in range(100):
    print(i)

# start, endを指定することも可能
for i in range(1, 101):
    print(i)

# ステップも指定可能
for i in range(1, 101, 2):
    print(i)

# 1から100までのリストを作成
my_list = range(1, 101)  # python2まで
my_list = list(range(1, 101))  # python3以降の書き方。パフォーマンス観点でリストを明示する必要がある

# enumerate を使うとindexも返すことができる
names = ['田中', '鈴木', '佐藤']
for index, name in enumerate(names):
    print('{0}番目は{1}'.format(index, name))

# zip で複数のリストを並列にアクセスできる
foods = ['納豆', 'ヨーグルト', 'チャーハン']
juices = ['コーラ', 'コーヒー', 'カフェラテ']
for food, juice in zip(foods, juices):
    print(food, juice)

# 要素数が異なる場合は、少ない方の配列分ループする
foods = ['納豆', 'ヨーグルト', 'チャーハン']
juices = ['コーラ', 'コーヒー']
for food, juice in zip(foods, juices):
    print(food, juice)
