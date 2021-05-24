# section13-1
# 타이핑 게임 기본

import random
import time

words = [] # 영어 단어 리스트(1000개 로드)

n = 1 # 게임 시도 횟수
cor_cnt = 0 # 정답 개수

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())

# 단어 목록 확인
# print(words)

# Enter Game Start!
input("Ready? Press Enter Key!\n")

start = time.time()

while n <= 5:
    random.shuffle(words)
    q = random.choice(words)

    print()

    print("*Question # {}".format(n))
    print(q)

    x = input()

    print()

    if str(q).strip() == str(x).strip():
        print("Pass!")
        cor_cnt += 1
    else:
        print("Wrong!")

    n += 1

end = time.time()
et = end - start
et = format(et, ".3f")

if cor_cnt >= 3:
    print("합격")
else:
    print("불합격")

print("게임 시간 : ", et, "초", "정답 개수: {}".format(cor_cnt))

if __name__ == '__main__':
    pass




