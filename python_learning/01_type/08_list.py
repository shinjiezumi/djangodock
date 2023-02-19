# list. 配列
my_list = [1, True, False, 'Python']  # どんな型でも格納できる。別の型でもOK
print(type(my_list))
print(my_list)

# 空のリスト
my_list = []
my_list = list()

# 文字列を分解して格納することも可能
my_list = list('Python')
print(my_list)  # ['P', 'y', 't', 'h', 'o', 'n']

# リストの追加
my_list = []
my_list.append('abc')
print(my_list)  # ['abc']
my_list.append('def')
print(my_list)  # ['abc', 'def']

my_list[0] = 'aaa'
print(my_list)  # ['aaa', 'def']

# 範囲指定して書き換えることも可能
my_list = [1, 2, 3, 4, 5]
my_list[:2] = [-1, -2]
print(my_list)  # [-1, -2, 3, 4, 5]
