# Section05-2
# 반복문 실습

# 기본 반복문 : for, while

v1 = 1
while v1 < 11:
    print("v1 is : ", v1)
    v1 += 1

for v2 in range(10):
    print("v2 is : ", v2)

for v3 in range(2,20,2):
    print("v2 is : ", v3)

sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1 ~ 100: ', sum1)
print('1 ~ 100: ', sum(range(1, 101)))
print('1 ~ 100: ', sum(range(1, 101, 2)))

# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable : range, reversed, enumerate, filter, map, zip

names = ["Kim", "Park", "Cho", "Choi", "Yoo"]

for name in names:
    print("You are name is", name)

word = "bass"

for s in word:
    print("Word : ", s)

my_info = {
    "name": "Kim",
    "age": 22,
    "city": "Seoul"
}

for k in my_info:
    print("my_info", k)

for k in my_info.keys():
    print("my_info", k)

for v in my_info.values():
    print("my_info", v)

for k, v in my_info.items():
    print("my_info", k, v)

name = "Andrew"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())

# break
numbers = [15, 16, 4, 13, 32, 14, 12, 67, 87, 99]

for num in numbers:
    if num == 32:
        print("found : 32")
        break
    else:
        print("not found : 32")

# for - else 구문(반복문이 정상적으로 수행된 경우 else 블럭 수행)
for num in numbers:
    if num == 2:
        print("found : 32")
        break
    else:
        print("not found : 32")
else:
    print("Not found 33......")

# continue

lt =["1", 2, 3, True, 4.7, complex(4)]

for v in lt:
    if type(v) is float:
        continue
    print("타입 :",type(v))