# 3で割り切れる場合は「Fizz」、5で割り切れる場合は「Buzz」、3と5で割り切れる場合は「FizzBuzz」、それ以外は数字を出力する

print(' '.join(['Fizz' * (num % 3 == 0) + 'Buzz' * (num % 5 == 0) or str(num) for num in
                range(1, 101)]))  # 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17..

fizz_buzz_list = ['Fizz' * (num % 3 == 0) + 'Buzz' * (num % 5 == 0) or str(num) for num in range(1, 101)]
result = ' '.join(fizz_buzz_list)
print(result)
