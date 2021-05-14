# Section07-1
# 파이쎤 클래스
# Self, 클래스, 인스턴스 변수

# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성 => 자바의 static
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용 => 자바의 일반 멤버 변수

# 선언
# class 클래스명:
#    함수
#    함수
#    함수

# 예제1
class UserInfo:
    # 속성, 메소드

    # 초기화 메소드, 자바의 생성자
    def __init__(self, name):
        self.name = name

    def user_info_p(self):
        print("Name: ", self.name)

# 네임스페이스, 클래스별로 가지고 있는 저장공간
user1 = UserInfo("Python")
user1.user_info_p()
user2 = UserInfo("Java")
user2.user_info_p()

# 인스턴스 주소
print(id(user1))
print(id(user2))

#네임스페이스 출력
print(user1.__dict__)
print(user2.__dict__)

# 예제2
# self의 이해
class SelfTest:
    def function1():
        print('function1 called!')

    def function2(self):
        print(id(self))
        print('function2 called!')

self_test = SelfTest()
self_test.function2()

# 자바의 정적 메소드 => self가 없는 것
SelfTest.function1()

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

    # 인스턴스 종료시 실행됨
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__) # 클래스 네임스페이스, 클래스 변수(공유)

print(user1.name)
print(user2.name)
print(user3.name)
print(WareHouse.stock_num)

# 인스턴스에 없으면 클래스 변수에서 찾는다.
print(user1.stock_num)

del user1

print(user2.stock_num)
print(user3.stock_num)
