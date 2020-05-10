# Section04-4
# 딕셔너리(Dictionary) : 순서x, 중복x, 수정o, 삭제o

# Key, Value, Json -> DB
# 선언
a = {'name': 'Kim', 'Phone': '010-8888-8888', 'birth': 780503}
b = {0: 'Hello', 1: 'Python', 2:'Code'}
c = {'arr': [1, 2, 3, 4, 5]}

print(type(a))

print(a['name'])
print(a.get('name'))
print(a.get('Tell'))
print(c['arr'][1:3])
print(c.get('arr'))
print('\n\n\n')

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 2, 3]
a['rank2'] = (1, 2)
print(a)
print('\n\n\n')

# keys, values, items
print(a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))

print(a.items())
print(list(a.items()))

print(1 in b)
print('name' in b)
print('name2' not in c)

# 집합(set) 순서x, 중복x
a = set()
b = set([1, 2, 3, 4])
c = set([1, 2, 2 ,3, 7])

print(type(a))
print(c)

t = tuple(b)
print(t)
l = list(b)
print(l)

print('\n\n\n')

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2)
print(s1.intersection(s2))

print(s1 | s2)
print(s1.union(s2))

print(s1 - s2)
print(s1.difference(s2))

# set 추가, 제거
s3 = set([7, 8, 10, 16])

s3.add(70)
s3.add(18)
s3.add(15)

print(s3)