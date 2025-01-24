# 自分の回答
d = {0: 'グー', 1: 'チョキ', 2: 'パー'}
options = tuple(d.keys())
while True:
    my_hand = input(f'自分が出す手を入力してください(整数 : 0, 1, 2)')
    if not my_hand.isdigit():
        print('整数の0, 1, 2を入力してください')
    else:
        my_hand = int(my_hand)
        if my_hand in options:
            print(f'自分が選んだ数字 : {my_hand}, 型 : {type(my_hand)}')
            break

# 回答
d = {0: 'グー', 1: 'チョキ', 2: 'パー'}
options = tuple(d.keys())

my_hand = 99
while my_hand not in options:
    my_hand = input(f'自分が出す手を入力してください(整数 : 0, 1, 2)')
    try:
        my_hand = int(my_hand)
    except:
        print('整数の0, 1, 2を入力してください。')

print(f'自分が選んだ数字 : {my_hand}, 型 : {type(my_hand)}')
