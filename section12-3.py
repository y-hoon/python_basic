# section12-3
# 파이썬 DB 연동(SQLite)

# 테이블 조회
import sqlite3

# DB파일 조회(없으면 새로 생성)
conn = sqlite3.connect('d:/study/python_basic/resource/database.db')

# Cursor 연결
c = conn.cursor()

# 데이터 수정 1
c.execute('update users set username = ? where id = ?', ('niceman', 2))

# 데이터 수정2
c.execute('update users set username = :name where id = :id', {"name": "goodman", "id": 5})

# 데이터 수정3
c.execute('update users set username = "%s" where id ="%s"' % ('good', 3))

# 중간 데이터 확인1
for user in c.execute('select * from users'):
    print(user)

# Row Delete1
c.execute('delete from users where id=?', (2,))

# Row Delete2
c.execute('delete from users where id= :id', {"id": 5})

# Row Delete3
c.execute('delete from users where id= "%s"' % 4)

print()
print()

# 중간 데이터 확인1
for user in c.execute('select * from users'):
    print(user)

# 테이블 전체 데이터 삭제
print("users db deleted : ", conn.execute('delete from users').rowcount, "rows")

# commit
conn.commit()

# 접속 해제
conn.close()