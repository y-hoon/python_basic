# section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트(순서 O, 중복 O, 수정 O, 삭제 O)

# 선언
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])
print(e[-1][-2])

# 슬라이싱
print(d[0:3])
print(e[2][1:3])

# 연산
print(c + d)
print(c * 3)
print(str(c[0]) + 'hi')

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)
c[1] = ['a', 'b', 'c']
print(c)

# index로 삭제
del c[1]
print(c)
del c[-1]
print(c)

# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6)
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2, 7)
print(y)
# 데이터의 값으로 삭제
y.remove(2)
print(y)
y.pop()
print(y)
ex = [88, 77]
# append는 리스트 자체를 삽입, extend는 원소로 삽입
y.extend(ex)
print(y)

# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트 자료형(순서O, 중복O, 수정O, 삭제O)

# 선언
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Cap', 'Plate']
e = [10, 100, ['Pen', 'Cap', 'Plate']]

# 인덱싱
print('#=====#')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', e[-1][1][2])
print('e - ', list(e[-1][1]))

# 슬라이싱
print('#=====#')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 리스트 연산
print('#=====#')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)
# print("c[0] + 'hi' - ",c[0] + 'hi')
print("'hi' + c[0] - ", 'hi' + str(c[0]))

# 리스트 수정, 삭제
print('#=====#')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c']
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[3]
print('c - ', c)

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(6)
print('a - ', a)
a.sort()
print('a - ', a)
a.reverse()
print('a - ', a)
print('a - ', a.index(5))
a.insert(2, 7)
print('a - ', a)
a.reverse()
a.remove(1)
print('a - ', a)
print('a - ', a.pop())
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4))
ex = [8, 9]
a.extend(ex)
print('a - ', a)

# 삭제 remove, pop, del

# 반복문 활용
while a:
    l = a.pop()
    print(2 == l)

# 튜플 자료형(순서O, 중복O, 수정X,삭제X)

# 선언
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, 'Pen', 'Cap', 'Plate')
e = (10, 100, ('Pen', 'Cap', 'Plate'))

# 인덱싱
print('#=====#')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', e[-1][1][2])
print('e - ', list(e[-1][1]))

# 슬라이싱
print('#=====#')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 튜플 연산
print('#=====#')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)
# print("c[0] + 'hi' - ",c[0] + 'hi')
print("'hi' + c[0] - ", 'hi' + str(c[0]))

# 튜플 함수
a = (5, 2, 3, 1, 4)

print('a - ', a)
print('a - ', a.index(5))
print('a - ', a.count(4))





