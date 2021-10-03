SELECT first_name, MAX(balance) FROM users_user
WHERE country='제주특별자치도';

SELECT first_name FROM users_user
ORDER BY balance DESC
LIMIT 1;