# format
def format_sample():
    fmt = '私の名前は{}です'
    name = '太郎'
    print(fmt.format(name))  # 「私の名前は太郎です」

    # 複数指定可能
    fmt = '私の名前は{} {}です'
    last_name = '山田'
    first_name = '太郎'
    print(fmt.format(last_name, first_name))  # 「私の名前は山田 太郎です」

    # 何番目の引数を埋め込むかも指定可能。文字列中で複数回引数を指定するときに利用
    fmt = '私の名前は{1} {0}です'
    print(fmt.format(last_name, first_name))  # 「私の名前は太郎 山田です」

    # キーワード引数
    fmt = '私の名前は{last_name2} {first_name2}です'
    print(fmt.format(last_name2='佐藤', first_name2='一郎'))  # 私の名前は佐藤 一郎です

    # python3.6からf stringsが使えるようになった
    last_name3 = '山本'
    first_name3 = '二郎'
    print(f'{last_name3} {first_name3}')  # 「山本 二郎」

    # 従来は%で指定していた。
    name2 = 'fugafuga'
    print('私の名前は%s' % name2)  # 「私の名前はfugafuga」


# split
def split_sample():
    languages = 'Python,Go,PHP,Javascript'
    lang_list = languages.split(',')  # ","で分割される。引数未指定の場合はスペースや改行、タブなどで分割される
    print(lang_list)  # ['Python', 'Go', 'PHP', 'Javascript']


# join
def join_sample():
    framework_list = ['Django', 'echo', 'Laravel', 'Rails']
    print(' '.join(framework_list))  # 「Django echo Laravel Rails」


def replace_sample():
    str = '今日は月曜日です'
    print(str.replace('月曜日', '水曜日'))  # 「今日は水曜日です」


# countでキーワードの出現回数を取得できる
def count_sample():
    str = '123454321'
    print(str.count('1'))  # 「2」


# 指定した文字列で始まっているかどうかを返す
def start_with_end_with_sample():
    name = 'hogefuga'
    print(name.startswith('hoge'))  # 「True」
    print(name.endswith('fuga'))  # 「True」


# キーワードが何文字目にあるかを走査する
def find_sample():
    name = 'yamada taro'
    print(name.find('amada'))  # 「1」
    print(name.find('taro'))  # 「7」
    print(name.find('hoge'))  # 見つからない場合は-1が返る

    # 単語が含まれているかどうかであればinメソッドが使える
    print(name in 'hoge')  # 「False」


# 先頭、末尾の空白を除去
def strip_sample():
    str = '  Hello World    '
    print(str.strip())

    # 先頭 or 末尾だけを除去することも可能
    print(str.rstrip())  # 「  Hello World」
    print(str.lstrip())  # 「Hello World    」


format_sample()
split_sample()
join_sample()
replace_sample()
count_sample()
start_with_end_with_sample()
find_sample()
strip_sample()
