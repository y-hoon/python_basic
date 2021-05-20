# section08
# 파이썬 모듈, 패키지

# 패키지 예제
# 상대 경로로 사용함

# 사용1(클래스)
# from 패키지명.파일명 import 클래스명

from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex2 : ", Fibonacci.fib2(400))
print("ex2 : ", Fibonacci().title)

# 사용2 (클래스) - 권장하지않음. 메모리를 사용1 보다 많이 사용, (자바와 동일 import *를 사용하지 않고 지정해서 import )
# from pkg.fibonacci import *

# 사용3 (클래스)
# from 패키지명.파일명 import 클래스명 as 별명
from pkg.fibonacci import Fibonacci as fb
print()
print()
fb.fib(300)

print("ex3 : ", fb.fib2(400))
print("ex3 : ", fb('alias fibonacci').title)


# 사용4(함수)
# import 패키지명.파일명 as 별명
import pkg.calculations as c
print()
print()
print("ex4 : ", c.add(10, 100))
print("ex4 : ", c.mul(10, 100))


# 사용5(함수)
# from 패키지명.파일명 import 함수명 as 별명
from pkg.calculations import div as d
print()
print()
print("ex5 : ", d(10, 100))


# 사용6
import pkg.prints as p
print()
print()
p.prt1()
p.prt2()

# builtins 은 기본으로 import되는 기능들임. import할 필요 없음
import builtins
print()
print()
print(dir(builtins))

