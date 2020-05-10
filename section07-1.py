# Section07-1
# 파이썬 클래스 상세 이해
# self, class, instance 변수

# 클래스, 인스턴스 차이
# 네임스페이스: 객체를 인스턴스화할 때 저장된 공간
# 클래스 변수: 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수: 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 선언
# class 클래스명:
#     함수
#     함수
#     함수

# 예제1
class UserInfo:
    # 속성과 메소드
    def __init__(self, name, height, weight): # class를 알리는 함수
        self.name = name
        self.height = height
        self.weight = weight
    def user_info_p(self):
        print("Name : ", self.name)
        print("Height : ", self.height)
        print("Weight : ", self.weight)
    

# 네임 스페이스
user1 = UserInfo("kim", "188", "89")
user1.user_info_p()
print(user1.name)

user2 = UserInfo("Park", "167", "46")
user2.user_info_p()
print(user2.name)

print(id(user1))
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)

# 예제2
# self의 이해

class SelfTest:
    def function1():
        print('func1 called!')
    def function2(self):
        print(id(self))
        print('func2 called!')

self_test = SelfTest()
SelfTest.function1()
self_test.function2()

print(id(self_test))
SelfTest.function2(self_test)

# 예제3
# 클래스 변수, 인스턴스 변수

class WareHouse:
    # 클래스 변수
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1

    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user1.__dict__)
print(user1.__dict__)
print(WareHouse.__dict__)

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num)
print(user2.stock_num)
print(user3.stock_num)

del user1

print(user2.stock_num)
print(user3.stock_num)