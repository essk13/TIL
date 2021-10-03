1. 전체 데이터 조회

   ```sqlite
   ORM
   User.objects.all()
   SQL
   SELECT * FROM users_user;
   ```

2. id가 19인 사람의 age 조회

   ```sqlite
   ORM
   User.objects.filter(id=19).values('age')
   SQL
   SELECT age FROM users_user
   WHERE id=19;
   ```

3. 모든 사람의 age 조회

   ```sqlite
   ORM
   User.objects.values('age')
   SQL
   SELECT age FROM users_user;
   ```

4. age가 40이하인 사람들의 id와 balance 조회

   ```sqlite
   ORM
   User.objects.filter(age__lte=40).values('id', 'balance')
   SQL
   SELECT id, balance FROM users_user
   WHERE age <= 40;
   ```

5. last_name이 '김'이고 balance가 500이상인 사람들의 first_name 조회

   ```sqlite
   ORM
   User.objects.filter(last_name='김', balance__gte=500).values('first_name')
   SQL
   SELECT first_name FROM users_user
   WHERE last_name='김' AND balance>=500;
   ```

6. first_name이 '수'로 끝나면서 행정구역이 '경기도'인 사람들의 balance 조회

   ```sqlite
   ORM
   User.objects.filter(first_name__endswith='수', country='경기도').values('balance')
   SQL
   SELECT balance FROM users_user
   WHERE first_name LIKE '%수' AND country='경기도';
   ```

7. balance가 2000이상이거나 age가 40이하인 사람의 총 인원수

   ```sqlite
   ORM
   User.objects.filter(Q(balance__gte=2000)|Q(age__lte=40)).count()
   SQL
   SELECT COUNT(*) FROM users_user
   WHERE balance >= 2000 OR age <= 40;
   ```

8. phone 앞자리가 010으로 시작하는 사람의 총 인원수

   ```sqlite
   ORM
   User.objects.filter(phone__startswith='010').count()
   SQL
   SELECT COUNT(*) FROM users_user
   WHERE phone LIKE '010%';
   ```

9. 이름이 '김옥자'인 사람의 행정구역을 경기도로 수정

   ```sqlite
   ORM
   User.objects.filter(first_name='옥자', last_name='김').update(country='경기도')
   
   User.objects.filter(first_name='옥자', last_name='김').values('country')
   SQL
   UPDATE users_user SET country='경기도'
   WHERE first_name = '옥자' AND last_name='김';
   
   SELECT country FROM users_user
   WHERE first_name = '옥자' AND last_name='김';
   ```

10. 이름이 '백진호'인 사람을 삭제하시오

    ```sqlite
    ORM
    User.objects.filter(first_name='진호', last_name='백').delete()
    
    User.objects.filter(first_name='진호', last_name='백').values()
    SQL
    DELETE FROM users_user
    WHERE first_name='진호' AND last_name='백';
    
    SELECT * FROM users_user
    WHERE first_name='진호' AND last_name='백';
    ```

11. balance를 기준으로 상위 4명의 first_name, last_name, balance 조회

    ```sqlite
    ORM
    User.objects.order_by('-balance').values('first_name', 'last_name', 'balance')[:4]
    SQL
    SELECT first_name, last_name, balance FROM users_user
    ORDER BY balance DESC
    LIMIT 4;
    ```

12. phone에 '123'을 포함하고 age가 30 미만인 정보 조회

    ```sqlite
    ORM
    User.objects.filter(phone__contains='123', age__lt=30).values()
    SQL
    SELECT * FROM users_user
    WHERE phone LIKE '%123%' AND age < 30;
    ```

13. phone이 '010'으로 시작하는 사람들의 행정 구역을 중복 없이 조회

    ```sqlite
    ORM
    User.objects.filter(phone__startswith='010').values('country').distinct()
    SQL
    SELECT DISTINCT country FROM users_user
    WHERE phone LIKE '010%';
    ```

14. 모든 인원의 평균 age

    ```sqlite
    ORM
    User.objects.aggregate(Avg('age'))
    SQL
    SELECT AVG(age) FROM users_user;
    ```

15. 박씨의 평균 balance

    ```sqlite
    ORM
    User.objects.filter(last_name='박').aggregate(Avg('balance'))
    SQL
    SELECT AVG(balance) FROM users_user
    WHERE last_name='박';
    ```

16. 경상북도에 사는 사람 중 가장 많은 balance

    ```sqlite
    ORM
    User.objects.filter(country='경상북도').aggregate(Max('balance'))
    SQL
    SELECT MAX(balance) FROM users_user
    WHERE country='경상북도';
    ```

17. 제주특별자치도에 사는 사람 중 balance가 가장 많은 사람의 first_name 조회

    ```sqlite
    ORM
    User.objects.filter(country='제주특별자치도').order_by('-balance').values('first_name')[:1]
    SQL
    SELECT first_name FROM users_user
    WHERE country='제주특별자치도'
    ORDER BY balance DESC
    LIMIT 1;
    ```