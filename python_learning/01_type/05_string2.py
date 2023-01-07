# 空文字
empty_str = ''
print(type(empty_str))

# 連結
address = '東京都'
address += '世田谷区'
print(address)  # 東京都世田谷区

# 連続文字を入力することも可能
hoge = 'hoge'
hoge *= 4
print(hoge)  # hogehogehogehoge

subject = '=' * 3 + ' タイトル ' + '=' * 3
print(subject)  # === タイトル ===

# 0を掛けると空文字になる
print("hoge: " + hoge)
hoge *= 0
print("hoge: " + hoge)

# 特殊文字
# 改行
str1 = 'hoge\nfuga'
print(str1)

# タブ
str2 = 'hoge\tfuga'
print(str2)

# 特殊文字を表示
str3 = 'hoge\\nfuga'
print(str3)

# 文字長
print(len("hogehoge"))

# dirで属性やメソッドを表示可能
hoge = 'hoge'
print(dir(hoge))

# ドットで参照できる
print(hoge.__class__)  # str
print(hoge.upper())  # HOGE
