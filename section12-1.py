# Section12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입
import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now: ', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime: ', nowDatetime)
print('sqlite3.version', sqlite3.version)
print('sqlite3.sqlite_version', sqlite3.sqlite_version)

# DB 생성 & Auto Commit (Rollback)
conn = sqlite3.connect('C:/Python_Project/resource/database.db', isolation_level = None)

# Cursor
c = conn.cursor()
print('Cursor Type: ', type(c))

# 테이블 생성(데이터 타입: Text, Numeric, integer, real, blob)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRMARY KEY, username text, email text, phone text, website text, regdate text)")

# 데이터 삽입
c.execute("INSERT INTO users VALUES(1, 'Kim', 'Kim@google.com', '000-1234-5678', 'Kim.com', ?)", (nowDatetime,))
c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", (2, 'Park', 'Park@naver.com', '010-5678-1234', 'Park.com', nowDatetime))

# Many 삽입(튜플, 리스트)
userList = (
    (3, 'Lee', 'Lee@daum.net', '010-3333-3333', 'Lee.com', nowDatetime),
    (4, 'Cho', 'Cho@google.com', '010-5555-5555', 'Cho.com', nowDatetime),
    (5, 'You', 'You@naver.com', '010-7777-7777', 'You.com', nowDatetime)
)

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", userList)

# 테이블 데이터 삭제
# conn.execute("DELETE FROM users")
# print("user db deleted :", conn.execute("DELETE FROM users").rowcount)

# 커밋 : isolation_level = None 일 경우 자동 반영(오토 커밋)
# conn.commit()

# 롤백
# conn.rollback()

# 접속 해제
conn.close()