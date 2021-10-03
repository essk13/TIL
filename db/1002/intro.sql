--  DB 생성
sqlite3 tutorial.sqlite3
sqlite> .database

-- CSV 파일 호출
sqlite> .mode csv
sqlite> .import users.csv examples

-- CREATE : 테이블 생성
-- PK 미지정 시 rowid(sqlite) 컬럼 자동 정의(명시를 위한 컬럼)
-- PK 지정 시 입력 간 PK를 제외한 컬럼 지정 후 입력시 PK 자동 생성
-- (AUTOINCREMENT) 속성 지정시 삭제 후 id(pk) 재사용 방지 가능
CREATE TABLE classmates (
  id INTEGER PRIMARY KEY,
  name TEXT
);

CREATE TABLE classmates (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT
);

CREATE TABLE classmates (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  address TEXT NOT NULL
);

-- DROP : 테이블 삭제
DROP TABLE classmates;

--------------- C R U D ---------------
-- INSERT : 데이터 저장(삽입)
-- 모든 컬럼에 데이터 저장 시 컬럼명 생략 가능
INSERT INTO classmates (name, age) VALUES ('홍길동', 20);

INSERT INTO classmates (name, age, address)
VALUES ('홍길동', 30, '서울');
== INSERT INTO classmates VALUES ('홍길동', 30, '서울');

INSERT INTO classmates (name, age, address)
VALUES ('김길동', 26, '부산');

INSERT INTO classmates VALUES
  ('홍길동', 30, '서울'),
  ('김철수', 30, '대전'),
  ('이사단', 26, '광주'),
  ('박상순', 29, '구미'),
  ('최종단', 28, '부산');

-- SELECT : 데이터 조회
SELECT * FROM classmates;
SELECT rowid, * FROM classmates;
-- (statment) 원하는 데이터만
SELECT rowid, name FROM classmates;
-- (LIMIT) 반환 개수 제한
SELECT rowid, name FROM classmates LIMIT 2;
-- (OFFSET) 탐색 시작 위치 지정 / 지정 숫자 만큼 제외하고 탐색
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
-- (WHERE) 탐색 조건 지정
SELECT rowid, name FROM classmates WHERE address=='서울';
-- (DISTINCT) 데이터를 중복 없이 조회
SELECT DISTINCT age FROM classmates;

-- UPDATE(+ SET / WHERE) : 데이터 수정
UPDATE classmates SET name='황길동', address='제주도' WHERE rowid=1;
UPDATE classmates SET name='최남단' WHERE rowid=5;

-- DELETE : 데이터(테이블) 삭제
-- DELETE(+ WHERE) : 데이터(행) 삭제
-- id(pk)는 삭제 후 데이터 저장 시 재사용 될 수 있음
DELETE FROM classmates WHERE rowid=6;



---------------실-------------습-----------------
-- 1) 테이브 생성
CREATE Table users(
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

-- 2) 데이터 불러오기
sqlite> .mode csv
sqlite> .import users.csv users

-- 3) age 30이상 유저의 모든 컬럼 정보 조회
SELECT * FROM users
WHERE age>=30;

-- 4) age 30이상 유저의 이름만 조회
SELECT first_name FROM users
WHERE age>=30;

-- 5) age 30이상, 성이 '김'인 사람의 나이와 성만 조회
SELECT age, last_name FROM users
WHERE age>=30
AND last_name='김';

-- 6) age 30이상 계좌 평균 잔액
SELECT AVG(balance) FROM users
WHERE age>=30;



-------------Functions---------------
-- COUNT : 레코드의 개수 조회
-- 레코드 총 개수
SELECT COUNT(*) FROM users;
-- 특정 데이터의 개수
SELECT COUNT(last_name) FROM users
WHERE last_name='김';

-- AVG, SUM, MIN, MAX : INTEGER 타입의 데이터 계산
SELECT AVG(age) FROM users 
WHERE age>=30;

SELECT SUM(age) FROM users 
WHERE age>=30;

SELECT first_name, MIN(age) FROM users;

SELECT first_name, MAX(balance) FROM users;


--------------------------------------------------
-- LIKE : 패턴 일치를 기반으로 데이터를 조회
-- (%) : 0개 이상
-- (_) : 1개
SELECT * FROM users
WHERE age
LIKE '2_';

SELECT * FROM users
WHERE first_name
LIKE '%준';

SELECT * FROM users
WHERE balance
LIKE '2%';

SELECT * FROM users
WHERE phone
LIKE '02-%';

SELECT * FROM users
WHERE phone
LIKE '%-5114-%';

-- ORDER BY : 조회 결과를 정렬
-- (ASC) : 오름차순 / default
-- (DESC) : 내림차순
SELECT * FROM users
ORDER BY age ASC
LIMIT 10;

SELECT * FROM users
ORDER BY age, last_name
LIMIT 10;

SELECT last_name, first_name FROM users
ORDER BY balance DESC
LIMIT 10;

SELECT first_name, age, balance FROM users
ORDER BY age, balance DESC;


-- GROUP BY : 지정한 기준에 따라 그룹 생성 / 데이터 요약 시 사용
-- AS를 활용하여 컬럼 명 변경 가능
SELECT last_name, COUNT(last_name) AS name_count FROM users
GROUP BY last_name;


--------------------------------------------------------------
-- ALTER TABLE : TABLE 수정
-- 1. 테이블 이름 수정
-- 2. 컬럼 추가
-- 3. 컬럼 이름 수정

-- 1) 테이블 생성
CREATE TABLE articles (
  title TEXT NOT NULL,
  content TEXT NOT NULL,
  updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- 2) 데이터 삽입
INSERT INTO articles VALUES ('1번제목', '1번내용');

-- 3) 테이블 이름 수정
ALTER TABLE articles
RENAME TO news;

-- 4) 컬럼 추가
-- 기존 데이터가 존재하면 NOT NULL 속성을 지닌 컬럼 추가시 에러 발생
-- NOT NULL 미지정 또는 DEFAULT 설정을 통해 해결 가능
ALTER TABLE news
ADD COLUMN created_at TEXT NOT NULL DEFAULT 'datetime';


