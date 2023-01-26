your_input = input('数字を入れてください >')

try:
    number = int(your_input)
    print(10 / number)
except ValueError:
    print('数字以外が入力されました')
except ZeroDivisionError:
    print('0が入力されました')
except:
    print('それ以外のエラー')

file = None
try:
    file = open('hello.txt', 'x', encoding='utf-8')
except FileExistsError:
    print('既に存在しています')
else:
    file.write('hello')
finally:
    if file is not None:
        file.close()
