members = {}


# クラス
class Student:
    def __init__(self, name):
        self.name = name
        self.score = {}

    def add_score(self, subject_name, score):
        self.score[subject_name] = score

    def get_score(self, subject_name):
        return self.score.get(subject_name, '教科未登録')


s = Student('sato')
s.add_score('math', 50)
print(s.get_score('math'))  # 50

members['sato'] = s

print(members)  # {'sato': <__main__.Student object at 0x104bcfc70>}


# 継承
class Character:
    def __init__(self, name):
        self.name = name

    def show_profile(self):
        profile = '名前{0} 種族:Character'.format(self.name)
        print(profile)


class Monster(Character):
    def show_profile(self):  # オーバーライド
        profile = '名前{0} 種族:Monster'.format(self.name)
        print(profile)

        super().show_profile()  # superで継承元を参照できる


char_a = Character('キャラA')
char_a.show_profile()

monster_a = Monster('モンスターA')
monster_a.show_profile()
