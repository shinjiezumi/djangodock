# ミュータブルとイミュータブル

|                 | ミュータブル？(変更可能)<br>イミュータブル？(変更孵化？) | シーケンス？<br>(添字でアクセスできる？) |
|-----------------|----------------------------------|-------------------------|
| 文字列(str型)       | イミュータブル                          | シーケンス                   |
| 数値(int, float型) | イミュータブル                          | ×                       |
| リスト(list型)      | ミュータブル                           | シーケンス                   |
| タプル(tuple型)     | イミュータブル                          | シーケンス                   |
| 辞書(dict型)       | ミュータブル                           | ×                       |
| セット(set型)       | ミュータブル                           | ×                       |

# pythonファイルについて

```python
#!/user/bin/env python
# -*- coding: utf-8 -*-


# １行目はシバン行. ファイル実行時にどのPythonインタプリタを使うのかの指定
# ２行目はマジックコメント。文字コード指定する。python3からはデフォルトがutf-8で動作するので記載不要。
```