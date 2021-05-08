# Section02-1
# Print
# 참조 : https://www.python-course.eu/python3_formatted_output.php

# 기본출력
print('Hello Python!')
print("Hello Python!")
print('''Hello Python!''')
print("""Hello Python!""")

# 출력값이 없을떄는 new line
print()

# Separator 옵션 사용, sep = '' => 작은 땨옴표로 묶은 값을 합쳐준다.
print('T', 'E', 'S', 'T')
print('T', 'E', 'S', 'T', sep='')
print('2021', '05', '05')
print('2021', '05', '05', sep='-')
print('niceman', 'google.com', sep='@')

# end 옵션 사용
print('Welcome To', end=' ')
print('the black paradise', end=' ')
print('piano notes')

print()

# format 사용, format은 파라미터별로 , 로 구분함
print('{} and {}'.format('You', 'Me'))
print('{0} and {1} and {0}'.format('You', 'Me'))
print('{a} are {b}'.format(a='You', b='Me'))

# %s : 문자, %d : 정수, %f : 실수
print("%s's favorite number is %d" % ('hoon', 5))

print()

print("Test1: %5d, Price: %4.2f" % (458, 6534.123))
print("Test1: {0: 5d}, Price: {1:4.2f}".format(458, 6534.123))
print("Test1: {a: 5d}, Price: {b:4.2f}".format(a=458, b=6534.123))

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
...

"""

print("'you'")
print('\'you\'')
print('"you"')
print("""'you'""")


