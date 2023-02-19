def file_write():
    # 書き込む内容
    text = """おはよう
    こんにちは
    こんばんは"""

    # ファイルを開く
    file = open('../hello.txt', 'w', encoding='utf-8')

    # ファイルに書き込み
    file.write(text)

    # ファイルを閉じる
    file.close()

    # 追記モードで開く
    text = '追記'
    file = open('../hello.txt', 'a', encoding='utf-8')
    file.write(text)
    file.close()

    # 'a'モードにすると、既にファイルがある場合はエラーになる
    # file = open('hello.txt', 'a', encoding='utf-8')

    # with を使うとcloseが不要になるので、基本的にこれを使う
    with open('../hello.txt', 'w', encoding='utf-8') as file:
        file.write(text)


def file_read():
    with open('../hello.txt', 'r', encoding='utf-8') as file:
        # 一気に読む
        src = file.read()
        print(src)

        # １行ずつ読み込む
        for line in file:
            print(line, end='')  # 自動で改行されるのでend を指定


# file_write()
file_read()
