import calc
import calc as c  # エイリアス
from calc import add  # インポートするものを指定することも可能

result = calc.add(1, 2)
print(result)

result = add(1, 2)
print(result)

result = c.add(1, 2)
print(result)
