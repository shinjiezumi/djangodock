from collections import Counter, defaultdict, OrderedDict

my_list = [1, 1, 1, 5, 1, 2, 5, 1]

counter = Counter(my_list)
print(counter.most_common())  # 出現回数を表示

my_dict = defaultdict(int)  # デフォルト値を持つ辞書
print(my_dict['hogehoge'])

my_dict = OrderedDict()  # 辞書に追加した順番を覚えている
my_dict['food'] = 'カレー'
my_dict['juice'] = 'コーラ'

for key, value in my_dict.items():
    print(key, value)
