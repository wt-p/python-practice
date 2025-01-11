# 自分の回答
phone_numbers = ['080-1203-4455', '090-9372-9682', '03-9471-5929', '070-3917-5918', '04-8572-8910']
new_l = []
phone_numbers_lists = ['090', '080', '070']
for v in phone_numbers:
    if v[0:3] in phone_numbers_lists:
        new_l.append(v)
print(f'携帯電話の番号 : {new_l}')

# 回答
phone_numbers = ['080-1203-4455', '090-9372-9682', '03-9471-5929', '070-3917-5918', '04-8572-8910']
new_l = [s for s in phone_numbers if s.find('-') == 3]
print(f'携帯電話の番号 : {new_l}')