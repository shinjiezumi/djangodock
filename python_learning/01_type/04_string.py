# 文字列
# ダブルクォート or シングルクォートで文字列
first_name = "hoge"
print(first_name)

first_name = 'fuga'
print(first_name)

number = 1
print(type(number))  # int

number_string = str(number)

print(type(number_string))  # str
print(number_string)

# 複数行文字列はダブルクォート or シングルクォート3つ
multi_line = """
hoge
fuga
"""

print(multi_line)

multi_line2 = '''
hoge2
fuga2
'''

print(multi_line2)

# 先頭、末尾に改行を入れない
multi_line3 = """\
hoge3
fuga3\
"""

print(multi_line3)
