# section10
# 파이썬 예외처리

# 예외 종류

# SyntaxError : 잘못된 문법

# print('Test)

# if True
#      pass

# NameError : 참조변수 없음

# a = 10
# b = 15
# print(c)

# ZeroDivisionError : 0 나누기 에러
# print(10 / 0)

# IndexError : 인덱스 범위 밖

# x = [10, 20, 30]
# print(x[3])

# KeyError : 없는 키를 조회할 때
dic = {'name': 'Kim', 'age': 40, 'City': 'Seoul'}
# print(dic['hobby'])
# 따라서 key 에러 방지를 위해 get 을 사용한다. 없으면 exception이 아니고 None를 리턴함
print(dic.get('hobby'))

# AttributeError : 모듈, 클래스에 없는 속성을 사용하려고 할 때
import time
print(time.time())
# print(time.month())

# ValueError : 참조 값이 없을 때 발생
x = [1, 5, 9]
# x.remove(10)
# x.index(10)

# FileNotFoundError
# f = open('test.txt', 'r')

# TypeError

x = [1, 2]
y = (1, 2)
z = 'test'
# print(x + y)
# print(x + z)

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생시 예외 처리 코딩 권장 (EAPP 코딩 스타일)

# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드를 감쌈
# except : 에러 catch
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# 예제1
name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim' # 없는 값을 하면 예외 발생
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError:
    print('Not found it! - Occurred ValueError!')
else:
    print('OK! else!')


# 예제2 - 에러를 특정하기 어려울때
# except ==== except Exception
try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except Exception:
    print('Not found it! - Occurred Error!')
else:
    print('OK! else!')


# 예제3
try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except:
    print('Not found it! - Occurred Error!')
else:
    print('OK! else!')
finally:
    print('finally ok!')


# 예제4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴(파이쎤에서 자주 사용!)
try:
    print('Try')
finally:
    print('OK Finally!!')

# 예제5
# 예외내용 출력
# except ValueError as l:
#     print(l)
try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError as l:
    print(l)
except IndexError:
    print('Not found it! - Occurred IndexError!')
except Exception:
    print('Not found it! - Occurred Exception!')
else:
    print('OK! else!')
finally:
    print('finally ok!')


# 예제 6
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생
try:
    a = 'Kim'
    if a == 'Kim':
        print('OK 허가!')
    else:
        raise ValueError
except ValueError:
    print('문제 발생!')
except Exception as f:
    print(f)
else:
    print('OK!')
