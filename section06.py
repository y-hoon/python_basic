# Section06
# 파이썬 함수식 및 람다 (lambda)

# 함수 정의 방법
# def 함수명(parameter):
#   code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요, 거의 대부분 언어에서 그렇듯이 선언을 먼저 해야 호출이 가능하다는 말

# 예제1
def hello(world):
    print("Hello", world)

hello("yhoon")

# 예제2
def hello_return(world):
    val = "Hello " + str(world)
    return val

str = hello_return("Python!!")
print("hello_return call : {}".format(str))

# 예제3 (다중리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(100)
print(val1, val2, val3)

# 예제4 (데이터 타입 반환)
# 리스트 리턴
def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

lt = func_mul2(100)
print(lt, type(lt))

# 튜플 리턴
def func_mul2t(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return (y1, y2, y3)


tup = func_mul2t(4)

print(type(tup), tup, list(tup))

# 딕셔너리 리턴
def func_mul3d(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return {'ret1': y1, 'ret2': y2, 'ret3': y3}


dic = func_mul3d(8)

print(type(dic), dic, dic.get('ret3'), dic.items(), dic.keys(), dic.values())



# 예제5
# * => tuple, ** => dictionary
# *args, *kwargs

# *args : 가번 파라미터. 자바의 ... 과 비슷
def args_func(*args):
    print(args)
    # tuple
    print(type(args))
    for t in args:
        print(t)
    # enumerate에 목록으로 표현되는 자료형을 넣으면
    # 인덱스값을 자동으로 생성해준다.
    for i, v in enumerate(args):
        print(i, v)


args_func('kim')
args_func('kim', 'Park')

# kwargs
def kwargs_func(**kwargs):
    print(kwargs)

    for k, v in kwargs.items():
        print("key:{}, value:{}".format(k, v))

kwargs_func(name1='kim', name2='Park')

# 전체 혼합, arg1, arg2는 단일 파라미터로, *args는 tuple로 **kwargs는 dictionary로
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10, 20)
example_mul(10, 20, 'park', 'kim')
example_mul(10, 20, 'park', 'kim', age1=24, age2=35)
example_mul(10, 20, age1=24, age2=35)

# 예제6
# 중첩함수(클로저)
def nested_func(num):
    def func_in_func(num):
        print(num)
    print("in func")
    func_in_func(num + 1000)

nested_func(10000)

# 예제7 : 힌트(Hint) - 파라미터나 리턴 타입을 표시해주는 기능
# parameter는 int이고 리턴 타입은 list라고 알려주는 기능임
# 잘못된 파라미터를 넣어도 오류가 발생하지는 않는다. 알려주기 위한 목적임
def func_mul3(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


def tot_length1(word: str, num: int) -> int:
    return len(word) * num

print('hint exam1 : ', tot_length1("i love you", 10))


def tot_length2(word: str, num: int) -> None:
    print('hint exam2 : ', len(word) * num)

tot_length2("niceman", 10)


# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# def mul_10(num):
#     return num * 10

# def mul_10_one(num): return num * 10
#
# lambda x: x * 10

# 일반적 함수 -> 변수 할당
def mul_10(num : int) -> int:
    return num * 10

var_func = mul_10
print(var_func)
print(type(var_func))

print(var_func(10))

# lambda num:num * 10 ---> 앞쪽의 num이 파라미터, 뒤쪽의 num * 10이 리턴
lambda_mul_10 = lambda num: num * 10

print("lambda result: {}".format(lambda_mul_10(10)))

# 함수를 파라미터로 넘기는 함수
def func_final(x, y, func):
    print(x * y * func(10))
    return x * y * func(10)

# 파라미터 함수에 람다를 넘긴다.
func_final(10, 10, lambda_mul_10)

print("parameter lambda: ", func_final(10, 10, lambda x: x * 1000))
