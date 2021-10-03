CREATE Table users(
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

INSERT INTO users VALUES (
  '창준', '이', '27', '경상북도', '000-0000-0000', 777777
  );

SELECT * FROM users WHERE first_name='창준';

SELECT first_name, last_name, age, balance FROM users
WHERE balance >= 400;

SELECT first_name, last_name, age, balance FROM users
WHERE balance >= 500 AND country='경상북도'
ORDER BY balance;

DELETE FROM users WHERE first_name='창준' AND balance=777777;

SELECT * FROM users
WHERE first_name='창준';

