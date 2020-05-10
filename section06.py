# Section06-1
# 함수 정의 및 람다

# 함수 정의 방법
# def fuction_name(parameter):
#   code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요

# 예제1
def hello(text):
    print("Hello", text)

hello("Python!")

# 예제2
def hello_return(text):
    val = "Hello " + str(text)
    return val

str = hello_return(999)
print(str)

# 예제3(다중 리턴)
def function_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300

    return y1, y2, y3

val1, val2, val3 = function_mul(3)
print(val1, val2, val3)

# 예제4(데이터 타입 반환)
def function_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300

    return [y1, y2, y3]

lst = function_mul2(100)
print(lst)

# 예제5
# *args, **kwargs

# args(tuple)

def args_fuction(*args):
    # for t in args:
    #     print(t)
    for i, v in enumerate(args):
        print(i, v)

args_fuction('kim')
args_fuction('Kim', 'Park')
args_fuction('Kim', 'Park', 'Lee')

# kwargs(dictionary)

def kwargs_function(**kwargs):
    for k, v in kwargs.items():
        print(k ,v)

kwargs_function(name1 = 'Kim', name2 = "Park")

# 전체 혼합
def ex_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

ex_mul(20, 10, 'Lee', 'Choi', age1 = 24, age = 34)

# 중첩 함수(클로저)

def nested_func(num):
    def func_in_func(num):
        print('>>>', num)
    print("in func")
    func_in_func(num + 1000)

nested_func(1000)

# 예제6(Hint)

def function_mul3(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300

    return [y1, y2, y3]

print(function_mul3(5))

# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(num : int) -> int:
        return num * 10

var_func = mul_10
print(var_func)
print(type(var_func))

print(var_func(10))

lambda_mul_10 = lambda x: x * 10
print('>>>',lambda_mul_10(10))

def func_final(x, y, func):
        print(x * y * func(10))

func_final(10, 10, lambda_mul_10)

print(func_final(10, 10, lambda x: x * 1000))