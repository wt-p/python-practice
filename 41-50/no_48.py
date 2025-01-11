# 自分の回答
telephone_numbers = ['080-1203-4455', '090-9372-9682', '090-3080-4982', '080-3917-5918']
new_l = []
for v in telephone_numbers:
    if v[0:3] == '080':
        new_l.append(v)
print(f'080で始まる電話番号 : {new_l}')

# 回答
telephone_numbers = ['080-1203-4455', '090-9372-9682', '090-3080-4982', '080-3917-5918']
new_l = [s for s in telephone_numbers if '080' in s[:3]]
print(f'080で始まる電話番号 : {new_l}')