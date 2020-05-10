# Section04-3
# 리스트(순서o, 중복o, 수정o, 삭제o)

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'PC', 'H/W', 'S/W']
e = [20, 200, ['PC', 'H/W', 'S/W']]

# 인덱싱

print(d[3])
print(d[-2])
print(d[0] + d[1])
print(e[2][1])
print(e[2][2])

# 슬라이싱

print(d[0:2])
print(e[2][1:3])

# 연산

print(c + d)
print(d + c)
print(c * 3)
print(str(c[0]) + 'pi')

# 리스트 수정, 삭제

c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)

c[1] = ['a', 'b', 'c']
print(c)

del c[1]
print(c)
print('\n\n\n')

# 리스트 함수

y = [5, 2, 3, 7, 9]
print(y)
y.append(0)
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2, 8)
print(y)
y.remove(5)
print(y)
y.pop()
print(y)

ex = [88, 77]
# y.extend(ex)
y.append(ex)
print(y)
print('\n\n\n')

# 튜플 (순서o, 중복o, 수정x, 삭제x)

a = ()
b = (1,9)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][1])
print(d[2][2]) 

print(d[2][:2])
print(d[2][-1])

print(c + d)
print(c * 3)
print('\n\n\n')

# 튜플 함수

z = (5, 2, 1, 3, 4)
print(z)
print(3 in z)
print(z.index(3))
print(z.index(5))
print(z.count(2))