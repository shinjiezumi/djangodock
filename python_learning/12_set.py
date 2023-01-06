# set. 集合
my_set = {1, 2, 3}
print(type(my_set))  # <class 'set'>
print(my_set)  # {1, 2, 3}

# 空のset
my_set = set()

# 配列から変換
my_list = [1, 2, 3]
my_set = set(my_list)
print(my_set)  # {1, 2, 3}

# 重複した値は削除される
my_list = [1, 1, 2, 3, 3]
my_set = set(my_list)
print(my_set)  # {1, 2, 3}

# add で追加
my_set.add(4)

# remove で削除
my_set.remove(1)

print(my_set)  # {2, 3, 4}

# in や len も使える
print(3 in my_set)  # True
print(len(my_set))  # 3
