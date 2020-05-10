# Section2-2
# 파이썬 기초
# 몸풀기 코딩

# import this
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print("My name is Python")

# 변수 선언
myname = "Java"

# 조건문
if myname == "Java":
    print("Ok!!")
else:
    print("No!!!")

print()

# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print("{} * {}".format(i, j))
    print()

print()

for i in range(1, 10):
    for j in range(1, 10):
        print("%d * %d" %(i, j))
    print()

# 함수
def func():
    print("Called func()")

func()

# 클래스
class Cookie():
    pass

# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))