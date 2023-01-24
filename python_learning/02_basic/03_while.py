#  while 条件式:
#   処理A

count = 0
while count < 10:
    print(count)
    count += 1

# flag = True
# while flag:
#     user_input = input()
#     if user_input == 'exit':
#         flag = False

# while True:
#     user_input = input()
#     if user_input == 'exit':
#         break
#     elif user_input == 'skip':
#         continue
#
#     message = '入力値は{0}でした'.format(user_input)
#     print(message)

names = ['田中太郎', '佐藤次郎', '鈴木三郎']
is_found = False
for name in names:
    if name.endswith('三郎'):
        is_found = True
        break

if is_found:
    print('居ました')
else:
    print('居ませんでした')

# ループでbreakがなかった時にelseが呼び出される. が、for elseやwhile elseは嫌う人も多いらしい
names = ['田中太郎', '佐藤次郎', '鈴木三郎']
for name in names:
    if name.endswith('三郎'):
        print('居ました')
        break
else:
    print('居ませんでした')
