# section09
# 파일 읽기,쓰기
# 읽기 모드 : r, 쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
# ..: 상대경로, . : 절대경로(context root)
# 기타 : https://docs.python.org/3.9/library/functions.html#open

# 파일 읽기
# 예제1
# open(파일경로)
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
print(dir(f))
# 반드시 close 리소스 반환
f.close()

print()
print()

# 예제2
# open, close필요없이 with로 사용
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print()
print()


# 예제3
# 한줄씩 읽어서 출력
with open('./resource/review.txt', 'r') as f:
    for c in f:
        # print(c) -> 마지막에 \n이 있어서 빈 라인이 하나 더 생김. 아래와 같이 하면(c.strip()) 원문과 동일해짐
        print(c.strip())

print()
print()

# 예제4
# read()로 cursor가 제일 뒤로 이동하였으므로 다시 read 하는 경우는 읽을 내용이 없다.
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read()  # 내용이 없음
    print(">", content)

print()
print()

# 예제5
# 한 줄씩 읽어오는 메소드 - readline
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    while line:
        print(line, end=' ')
        line = f.readline()

print()
print()

# 예제6
# readlines - 한 줄씩 읽어서 list에 저장(각 줄이 list의 요소가 됨)
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    for c in contents:
        print(c, end= ' *** ')

print()
print()

# 예제7
# 파일을 오픈하면 iterable하니까 바로 한 줄씩 읽는다.
score = []
with open('./resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)

print('Average : {:6.3}'.format(sum(score)/len(score)))


# 파일 쓰기

# 예제1
with open('./resource/text1.txt', 'w') as f:
    f.write('Niceman!\n')


# 예제2
with open('./resource/text1.txt', 'a') as f:
    f.write('Goodman!\n')


# 예제3
from random import randint
with open('./resource/text2.txt', 'a') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write('\n')


# 예제4
# writelines : 리스트 -> 파일로 저장
with open('./resource/text3.txt', 'a') as f:
    list = ['Kim\n', 'Lee\n', 'Park\n']
    f.writelines(list)


# 예제5
# print문을 사용해서 파일에 저장
with open('./resource/text4.txt', 'a') as f:
    print('Test Contents1!', file=f)
    print('Test Contents2!', file=f)

