# 自分の回答
l = [{'id': 10000, 'feature': {'name': 'Michael', 'height': 180.3, 'weight': 63.7, 'skills': {'IT': ['Python', 'Golang', 'SQL'], 'Others': ['Chinese', 'Math']}}},
{'id': 10001, 'feature': {'name': 'Nancy', 'height': 156.7, 'weight': 39.7, 'skills': {'IT': ['Java', 'SQL', 'JavaScript'], 'Others': ['Accounting']}}}]
skill1 = l[0]['feature']['skills']
skill2 = l[1]['feature']['skills']
a = {}
for k1, v1 in skill1.items():
    for k2, v2 in skill2.items():
        if set(v1) & set(v2):
            a = set(v1) & set(v2)
print(f'共通するITスキル : {a}')

# 回答
l = [{'id': 10000, 'feature': {'name': 'Michael', 'height': 180.3, 'weight': 63.7, 'skills': {'IT': ['Python', 'Golang', 'SQL'], 'Others': ['Chinese', 'Math']}}},
{'id': 10001, 'feature': {'name': 'Nancy', 'height': 156.7, 'weight': 39.7, 'skills': {'IT': ['Java', 'SQL', 'JavaScript'], 'Others': ['Accounting']}}}]

it_skills = [d['feature']['skills']['IT'] for d in l]
print(it_skills)
michael_skill, nancy_skill = it_skills
common_sill = set(michael_skill) & set(nancy_skill)
print(f'共通するITスキル : {common_sill}')
