from pathlib import Path

# カレントディレクトリ
current = Path()
for path in current.iterdir():
    print(path.resolve())  # 絶対パスで表示
    if path.is_dir():
        for p in path.iterdir():
            print(p)

a = Path('a.txt')
with a.open('w', encoding='utf-8') as file:
    file.write('hello')
