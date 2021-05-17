# Section07-2
# 파이썬 클래스 상속, 다중상속

# 예제1
# 상속 기본

class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class "Show Method!"'

# 파이썬에서의 상속 - 클래스명(부모클래스) - BmwCar(Car)
class BmwCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name


class BenzCar(Car):
    """Sub Class"""

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

    def show(self):
        print(super().show())
        return 'Car Info : %s, %s, %s' % (self.car_name, self.type, self.color)

# 일반 사용
model1 = BmwCar('520d', 'Sedan', 'red')

print(model1.color)
print(model1.type)
print(model1.car_name)
print(model1.show())
print(model1.show_model())
print(model1.__dict__)

# Method Overriding
model2 = BenzCar('S450', 'SUV', 'White')
print(model2.show())

# Parent Metohd Call
model3 = BenzCar('C220', 'Sedan', 'Blue')
print(model3.show())

# Inheritance Info - list로 보여줌
print(BmwCar.mro())
print(BenzCar.mro())

# 예제2
# 다중 상속
class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

print()
print()
print(M.mro())
print()
print()
print(A.mro())
