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
