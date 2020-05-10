# Section04-2
# 문자열, 문자열 연산, 슬라이싱

str1 = "I am Programmer."
str2 = "PC"
str3 = ' '
str4 = str('        ')

print(len(str1), len(str2), len(str3), len(str4))

escape_str1 = "Do you know \"Programming Language C++\""
print(escape_str1, len(escape_str1))
escape_str2 = "Tab\tTab\tTab\n"
print(escape_str2)

# Raw String
raw_s1 = r'C:\programs\test'
print(raw_s1)
raw_s2 = r'a\\a\\a\\a'
print(raw_s2)

# 멀티라인
multi = \
"""
문자열
멀티라인
테스트
"""

print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = 'def'
str_o4 = 'Programmer'

print(str_o1 * 10)
print(str_o2 + str_o3)
print(str_o2 * 3)
print('a' in str_o4)
print('f' in str_o4)
print('z' not in str_o4)

# 문자열 형 변환
print(str(66) + 'a')
print(str(10.4))

# 문자열 함수

# a = 'program'
# b = 'Software'

# print(a.islower())      # 문자 a가 소문자로 이루어져 있는지
# print(b.endswith('e'))  # 문자 b가 끝나는 문자가 e인지
# print(a.capitalize())
# print(a.replace('program', 'macine'))
# print(list(reversed(b)))

a = 'program'
b = 'software'

print(a[0:3])
print(b[0:3])
print(b[0:4])
print(a[0:len(a)])
print(a[:])
print(b[:4])
print(b[-1])
print(b[0:4:2])
print(b[1:-2])
print(b[::-1])