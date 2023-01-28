import datetime

# 日時の作成
date = datetime.datetime(year=2022, month=12, day=30, hour=12, minute=0, second=0)
print(date)

# 3日後の日時
delta = datetime.timedelta(days=3)
print(date + delta)

# フォーマット出力
message = '{0.year}年{0.month}月{0.day}日'.format(date)
print(message)  # 2022年12月30日
