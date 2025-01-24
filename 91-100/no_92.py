# 自分の回答
import random

d = {0: 'グー', 1: 'チョキ', 2: 'パー'}
options = tuple(d.keys())
computer_hand = random.choice(options)

my_hand = 99
while my_hand not in options:
    my_hand = input(f'自分が出す手を入力してください(整数 : 0, 1, 2)')
    try:
        my_hand = int(my_hand)
    except:
        print('整数の0, 1, 2を入力してください。')

print(f'コンピューターの出した手 : {d[computer_hand]}')
print(f'自分の出した手 : {d[my_hand]}')

# 回答
import random

d = {0: 'グー', 1: 'チョキ', 2: 'パー'}
options = tuple(d.keys())
computer_hand = random.choice(options)

my_hand = 99
while my_hand not in options:
    my_hand = input(f'自分が出す手を入力してください(整数 : 0, 1, 2)')
    try:
        my_hand = int(my_hand)
    except:
        print('整数の0, 1, 2を入力してください。')

print(f'コンピューターが出した手 : {d[computer_hand]}')
print(f'自分が出した手 : {d[my_hand]}')
