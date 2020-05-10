# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for k in q1.keys():
    if k == "가을":
        print(q1[k])

for k, v in q1.items():
    if k == "가을":
        print(v)
        break

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for k, v in q2.items():
    if v == "사과":
        print("해당 과일이 있습니다.")
        break

else:
    print("사과 없음")

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

# i = input("점수를 입력하세요: ")
# num = int(i)

# if num <= 100 and num > 80:
#     print("A학점")
# elif num <= 80 and num > 60:
#     print("B학점")
# elif num <= 60 and num > 40:
#     print("C학점")
# elif num <= 40 and num > 21:
#     print("D학점")
# else:
#     print("E학점")

# if i >= 81:
#     print("A학점")
# elif a >= 61:
#     print("B학점")
# elif a >= 41:
#     print("C학점")
# elif a >= 21:
#     print("D학점")
# else:
#     print("E학점")

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
n1 = 12
n2 = 6
n3 = 18

if n1 > n2:
    if n2 > n3:
        print("가장 큰 수 :", n1)
    elif n3 > n2:
        if n1 > n3:
            print("가장 큰 수 :", n1)
        else:
            print("가장 큰 수 :", n3)


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
# i2 = input("주민번호 뒷자리를 입력하세요: ")

# if i2[0] == str(1) or i2[0] == str(3):
#     print("남자입니다.")
# elif i2[0] == str(2) or i2[0] == str(4):
#     print("여자입니다.")


# 6 ~ 10 반복문 사용(while 또는 for)
for i in range(6,11):
    print(i, "번")


# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

for v2 in q3:
    if v2 == "정":
        continue
    else:
        print(v2)

print()

ex = [x for x in q3 if x != '정']
print(ex)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
# for i in range(1,99,2):
#     print("홀수: ", i+2)

for n in range(1,101):
    if n % 2 == 1:
        print(n, end = ', ')

print()

ex2 = [x for x in range(1,101) if x%2 == 1]
print(ex2)

print()
# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

for idx in range(len(q4)):
    if len(q4[idx]) >= 5:
        print(q4[idx], end=', ')

print()
# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]


for v3 in q5:
    if v3.isupper():
        print(v3.lower(), end=' ')
    else:
        print(v3.upper(), end = ' ')
    
for idx2 in range(8):
    if q5[idx2].upper() == q5[idx2]:
        continue
    else:
        print(q5[idx2])
    # elif q5[idx2].upper() != q5[idx2]:
    #     print(q5[idx2])
     

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for idx3 in range(len(q6)):
    # if q6[idx3].upper() == q6[idx3]:
    #     print(q6[idx3].lower())
    # else:
    #     print(q6[idx3].upper())
    # elif q6[idx3].lower() == q6[idx3]:
    #     print(q6[idx3].upper())

    if q6[idx3].lower() == q6[idx3]:
        print(q6[idx3].upper())
    else:
        print(q6[idx3].lower())

# 1 ~ 100까지 출력하는 방법
number = [x for x in range(1,101)]
print(number)