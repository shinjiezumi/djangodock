def my_sort(string):
    return string[-1]


my_list = ['python', 'django', 'javascript', 'go']

# 昇順でソート
my_list.sort()
print(my_list)

# 最後の文字でソート
my_list.sort(key=my_sort)
print(my_list)


# 価格でソート
def price_sort(tpl):
    return tpl[1]


products = [('納豆', 70), ('ヨーグルト', 90), ('コーヒー', 120), ('さば缶', 100)]
products.sort(key=price_sort)
print(products)  # [('納豆', 70), ('ヨーグルト', 90), ('さば缶', 100), ('コーヒー', 120)]

# lamda関数を使うとソート関数が不要になる
# lamda 引数:返す値(何でソートするか)
products.sort(key=lambda tpl: tpl[1])
print(products)
