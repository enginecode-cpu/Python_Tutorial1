# Section02-1
# 파이썬 기초
# print 구문의 이해

# 기본 출력
print("Hello Python!")
print('Hello Python!')
print("""Hello Python!""")
print('''Hello Python!''')
print()

# Separator 옵션 사용
print('P', 'Y', 'T', 'H', 'O', 'N')
print('P', 'Y', 'T', 'H', 'O', 'N', sep="")
print("2020", "05", "10", sep='-')
print("test", "google.com", sep='@')

# end 옵션 사용
print("Welcome to", end=' ')
print("the Python World")
print()

# format 사용
print("{} or {}".format("apple", "melon"))
print("{0} or {1} or {0}".format("apple", "melon"))
print("{a} or {b}".format(a="apple", b="melon"))
print()

print("Test1 : %5d, Price : %4.2f" %(123, 7890.1234)) # 5자리의 정수가 온다는 것을 의미, 소수점을 둘째자리까지만 출력
print("Test1 : {0: 5d}, Price : {1: 4.2f}".format(123, 7890.1234))
print("Test1 : {a: 5d}, Price : {b: 4.2f}".format(a=123, b=7890.1234))
print()

# 이스케이프 코드
"""
\n : 줄 바꿈
\t : 탭
\\ : '\' 추가
\' : 작은 따옴표 추가
\" : 큰 따옴표 추가

"""

print("'You'")
print('\'You\'')
print('"You"')
print("""'You'""")
print("\\You\\\n")
print("\t\t\ttest")