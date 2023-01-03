# tuple
my_tuple1 = ()
my_tuple2 = tuple()
my_tuple3 = (1, True, False, 'Python')

my_tuple4 = 1, True, False, 'Python'  # 括弧を省略しても初期化される
print(type(my_tuple4))  # 「<class 'tuple'>」」

# 末尾にカンマがあればタプルになる
my_tuple5 = 'Python',
print(type(my_tuple5))  # 「<class 'tuple'>」」

# 各要素の参照やスライス処理もリストと同様に行える
my_tuple6 = 'Python', 'PHP', 'Ruby', 'Perl'
print(my_tuple6[1])  # 「PHP」

# リストと違いタプルは要素の中身や追加が変更ができない
# my_tuple6[1] = 'Javascript' # error

'''
# タプルの利点
・パフォーマンスがリストより優れている
・イミューテブルなので値が変更されないことが保証されている
'''
