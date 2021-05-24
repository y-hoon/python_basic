# section12-2
# 파이썬 DB 연동(SQLite)

# 테이블 조회
import sqlite3

# DB파일 조회(없으면 새로 생성)
conn = sqlite3.connect('d:/study/python_basic/resource/database.db')

# cursor 바인딩
c = conn.cursor()

# 데이터 조회(전체)

c.execute("select * from users")

# 커서 위치 변경
# 1개 row 선택
# print('One -> \n', c.fetchone())

# 지정 로우 선택
# print('Three -> \n', c.fetchmany(size=3))

# 전체 로우 선택
# print('All -> \n', c.fetchall())

# cursor의 위치가 제일 마지막이면 빈 리스트 리턴됨 ==> []
# print('All again -> \n', c.fetchall())

# 순회 1
# rows = c.fetchall()
# for row in rows:
#     print('retrieve1 > ', row)

# 순회 2
# for row in c.fetchall():
#     print('retrieve2 > ', row)

# 순회 3
for row in c.execute('select * from users order by id desc'):
    print('retrieve3 > ', row)


print()
print()

# WHERE Retrieve1
param1 = (3,)
c.execute('select * from users where id=?', param1)
print('param1', c.fetchone())
print('param1', c.fetchall()) # 데이터 없음


# WHERE Retrieve2
param2 = 4
c.execute('select * from users where id="%s"' % param2)
print('param2', c.fetchone())
print('param2', c.fetchall()) # 데이터 없음


# WHERE Retrieve3
c.execute('select * from users where id=:Id', {"Id": 5})
print('param3', c.fetchone())
print('param3', c.fetchall()) # 데이터 없음


# WHERE Retrieve4
param4 = (3,5)
c.execute('select * from users where id in (?, ?)', param4)
print('param4', c.fetchall())


# WHERE Retrieve5
c.execute('select * from users where id in ("%d", "%d")'% (3, 4))
print('param5', c.fetchall())


# WHERE Retrieve6
c.execute('select * from users where id = :id1 OR id = :id2', {"id1": 2, "id2": 1})
print('param6', c.fetchall())


# Dump 출력
with conn:
    with open('d:/study/python_basic/resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete')








