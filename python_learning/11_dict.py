# dict
score = {'math': 80, 'science': 50}
print(type(score))  # <class 'dict'>

# 空の辞書
score = {}
score = dict()

# リストから変換(あまり使わない)
names = [['佐藤', '太郎'], ['鈴木', '一郎']]
name_dict = dict(names)

print(name_dict)  # {'佐藤': '太郎', '鈴木': '一郎'}

# key名で参照できるが、存在しないkey名を指定するとエラーとなる
score = {'math': 80, 'science': 50}
print(score['math'])  # 80

# get を使うと初期値を指定できる
math = score.get('math', 'データなし')
print(math)

hoge = score.get('hoge')
print(hoge)  # 未指定の場合はNoneが返る

# update でマージができる。keyが重複する場合は上書きされる
band_menbers = {'ギター': '佐藤', 'ベース': '吉田'}
new_menbers = {'ドラム': '斉藤', 'ボーカル': '田中'}
band_menbers.update(new_menbers)

print(band_menbers)  # {'ギター': '佐藤', 'ベース': '吉田', 'ドラム': '斉藤', 'ボーカル': '田中'}

# popで削除できる
deleted = band_menbers.pop('ギター')
print(band_menbers)  # {'ベース': '吉田', 'ドラム': '斉藤', 'ボーカル': '田中'}
print(deleted)  # 佐藤

# in や len も使える
print('ベース' in band_menbers)  # True
print('キーボード' in band_menbers)  # False
print(len(band_menbers))  # 3

# setdefault で初期値も指定できる
band_menbers.setdefault('音響', '原田')
print(band_menbers.get('音響'))  # 原田

# keys, values, items で一覧を取得できる。厳密にはリストではない(メモリ使用量の観点で)
print(band_menbers.items())  # dict_items([('ベース', '吉田'), ('ドラム', '斉藤'), ('ボーカル', '田中'), ('音響', '原田')])
print(band_menbers.keys())  # dict_keys(['ベース', 'ドラム', 'ボーカル', '音響'])
print(band_menbers.values())  # dict_values(['吉田', '斉藤', '田中', '原田'])
