# Section05-1
# 조건문 실습

print(type(True))
print(type(False))

# 예1
if True:
    print("True")

# 예2
if False:
    print("False")
else:
    print("Here True")

# 관계 연산자
# >, >=, <, <=, ==, !=
a = 10
b = 0

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

# 참 거짓 종류(True, False)
# 참: "내용", [내용], (내용), {내용}, 1
# 거짓: "", [], (), {}

city = ''

if city:
    print(">>>>>True")
else:
    print(">>>>>False")

# 논리 연산자
# and or not

a = 100
b = 60
c = 15
print('and : ', a > b and a < c)
print('or : ', a > b or c > a)
print('not : ', not False)

# 산술, 관계, 논리 연산자
# 산술 > 관계 > 논리 연산자
print('ex1 : ', 5 + 10 > 0 and not 7 +3 == 10)

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print("합격!!")
else:
    print("불합")

# 다중 조건문
num = 90

if num >= 90:
    print("num 등급 A", num)
elif num >= 80:
    print("num 등급 B", num)
elif num >= 70:
    print("num 등급 C", num)
else:
    print("꽝!")

# 중첩 조건문
age = 25
height = 180

if age >= 20:
    if height >= 175:
        print("1지망 지원 가능")
    elif height >= 160:
        print("2지망 지원 가능")
    else:
        print("지원 불가")
else:
    print("20세 이상 지원 가능")