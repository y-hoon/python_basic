# section02-2
# 파이썬 기초
# 몸풀기 코딩

# 파이쎤 철학 출력
# import this
import sys

# 파이썬 기본 인코딩 확인
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print('My name is y-hoon!')

# 변수 선언
myName = 'y-hoon'

# 조건문
if myName == 'y-hoon':
    print('OK')

# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' % (i, j), i * j)


# 함수 선언
def greeting():
    print("안녕하세요. 반갑습니다.")


greeting()


# 클래스
class Cookie:
    pass


# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))
