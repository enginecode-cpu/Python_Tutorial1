# 데이터 타입

v_str1 = 'NiceMan'
v_bool = True
v_str2 = 'Good boy'
v_float = 10.3
v_int = 7
v_dict = {"name" : "Kim", "age" : 25}
v_tuple = 3, 5, 7
v_set = {7, 9, 10}
v_list = [1, 5, 6]

print(type(v_str1))
print(type(v_bool))
print(type(v_str2))
print(type(v_float))
print(type(v_int))
print(type(v_dict))
print(type(v_tuple))
print(type(v_list))

# 파이썬 숫자형 및 연산자
i1 = 39
i2 = 939
big_int1 = 9999
big_int2 = 7777
f1 = 1.234
f2 = 3.146
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2)
print(i1 ** f3)
print(f3 + i1)

result = f3 + i1
print(result, type(result))

a = 5.
b = 4
c = 10
d = 3

result2 = a + b
print(result2)

# 형 변환
# int, float, boolean, complex

print(int(result2))
print(float(c))
print(complex(d))
print(int(True))
print(int(False))
print(int('3'))

# 수치 연산 함수

print(abs(-7))
n, m = divmod(100, 8)
print(n, m)

import math

print(math.ceil(5.1))   # 5.1 이상이면서 가장 작은 정수
print(math.floor(3.8))  # 3.8 이하이면서 가장 큰 정수

