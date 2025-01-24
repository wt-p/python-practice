# 自分の回答
import random

d = {0: 'グー', 1: 'チョキ', 2: 'パー'}
options = tuple(d.keys())
computer_hand = random.choice(options)

print('*'*10 + f'\n選択肢 : {d}\n' + '*'*10)

my_hand = 99
while my_hand not in options:
    my_hand = input(f'自分が出す手を入力してください(整数 : 0, 1, 2)')
    try:
        my_hand = int(my_hand)
    except:
        print('整数の0, 1, 2を入力してください。')

result = ''
if my_hand == computer_hand:
    result = '引き分け'
elif my_hand - computer_hand == -1 or my_hand - computer_hand == 2:
    result = '勝ち'
elif my_hand - computer_hand == -2 or my_hand - computer_hand == 1:
    result = '負け'
print(f'コンピューターの出した手 : {d[computer_hand]}')
print(f'自分の出した手 : {d[my_hand]}')
print(f'結果 : {result}')

# 回答
import random

d = {0: 'グー', 1: 'チョキ', 2: 'パー'}
options = tuple(d.keys())
computer_hand = random.choice(options)

print('*'*10 + f'\n選択肢 : {d}\n' + '*'*10)

my_hand = 99
while my_hand not in options:
    my_hand = input(f'自分が出す手を入力してください(整数 : 0, 1, 2)')
    try:
        my_hand = int(my_hand)
    except:
        print('整数の0, 1, 2を入力してください。')

print(f'コンピューターの出した手 : {d[computer_hand]}')
print(f'自分の出した手 : {d[my_hand]}')

is_win = False
if computer_hand == my_hand:
    is_win = 'あいこ'
else:
    if computer_hand == 0 and my_hand == 2:
        is_win = True
    elif computer_hand == 1 and my_hand == 0:
        is_win = True
    elif computer_hand == 2 and my_hand == 1:
        is_win =True

if isinstance(is_win, bool):
    is_win = '勝ち' if is_win else '負け'

print(f'結果 : {is_win}')
