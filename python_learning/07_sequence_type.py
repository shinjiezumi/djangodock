# シーケンス型は配列のように参照することが可能
text = 'あいうえお'
print(text[2])  # 「う」

# マイナス値を指定すると末尾の文字から参照可能
print(text[-1])  # 「お」
print(text[-2])  # 「え」

# 「start:end」範囲指定して取得することも可能
print(text[2:4])  # 添字2(3文字目)から4文字目まで取得。「うえ」

# endを省略すると末尾まで取得可能
print(text[2:])  # 「うえお」

# 同様にstartも省略可能
print(text[:3])  # 「あいう」

# マイナス値だと末尾から取得
print(text[-3:])  # 「うえお」

# 「:」2つでx文字ごとに取得可能
print(text[::2])  # 「あうお」

# さらに-1を指定すると文字列を逆にすることができる
print(text[::-1])  # 「おえういあ」
