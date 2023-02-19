# if 条件式:
#   処理A

names = ['田中', '吉田', '佐藤']
if '田中' in names:
    print('田中さんがいました')
else:
    print('田中さんはいません')

# 比較演算子
color = 'red'
if color == 'red':
    print('赤色です')
elif color == 'blue':
    print('青色です')

# ブール演算子
numbers = [1, 2, 3, 4, 5]
if 1 in numbers and 2 in numbers:
    print('1と2が含まれています')

if 100 in numbers or 1 in numbers:
    print('1か100が含まれています')

if 100 not in numbers:
    print('100は含まれていません')

# 空かどうかはlen ではなく省略形が推奨されている
if numbers:
    print('numbersは空ではありません')
