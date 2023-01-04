# 便利な関数
numbers = [1, 2, 3, 4, 5]

print(len(numbers))  # 5

print(sum(numbers))  # 15

print(max(numbers))  # 5

print(min(numbers))  # 1

# 要素の追加
## insert で任意の要素に追加できる
numbers.insert(1, 1.5)  # 要素, 値を指定
print(numbers)  # [1, 1.5, 2, 3, 4, 5]

## リストを合体する
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers1.extend(numbers2)

print(numbers1)  # [1, 2, 3, 4, 5, 6]

## +で繋げることも可能
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers3 = numbers1 + numbers2
print(numbers3)  # [1, 2, 3, 4, 5, 6]

# 要素の削除
## pop で末尾を削除
numbers = [1, 2, 3, 4, 5]
deleted = numbers.pop()
print(numbers)  # [2, 3, 4, 5]
print(deleted)  # 1

## remove で指定した要素を削除
alphabets = ['a', 'b', 'c']
alphabets.remove('b')
print(alphabets)  # ['a', 'c']

## index でリストの何番目にあるかわかる
alphabets = ['a', 'b', 'c']
print(alphabets.index('c'))  # 2

## in で含まれているかがわかる
numbers = [1, 2, 3, 4, 5]
print(1 in numbers)  # True
print(100 in numbers)  # False

## count で出現回数がわかる
numbers = [1, 2, 2, 3, 4, 5]
print(numbers.count(2))  # 2

## join で文字列として連結
my_list = ['おはよう', 'こんにちは', 'こんばんは']
print('\n'.join(my_list))  # おはよう\nこんにちは\nこんばんは

## sort で並び替え
numbers = [3, 2, 4, 1, 5]
numbers.sort()
print(numbers)  # [1, 2, 3, 4, 5]

## reverse 引数で降順に
numbers.sort(reverse=True)
print(numbers)  # [5, 4, 3, 2, 1]

## sorted で別のリストを返す
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 2, 3, 4, 5]
print(numbers)  # [5, 4, 3, 2, 1]. 降順のまま

## copy でコピーが作成できる
copied = numbers.copy()
print(copied)
