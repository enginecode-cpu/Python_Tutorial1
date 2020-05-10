# 부록
# lambda, map 함수 익히기

# lambda 함수
# 10을 더하는 것
plus_ten = lambda x:x+10

print(plus_ten(1))

# 10을 곱하는 것
multiplication_ten = lambda x: x*10
print(multiplication_ten(3))

# map 함수
# map 함수는 두 번쨰 인자에 반복 가능한 것을 넣으면 된다.
print(list(map(lambda x:x+10, [1, 2, 3])))

print(list(map(lambda x:x*10, [4, 5, 6])))

# A-Z까지 출력하고 옆에 index를 표시해준다.
char_table = list(map(lambda x: (chr(x+65), x), range(26)))
print(char_table)
