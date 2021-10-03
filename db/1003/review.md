1. ```sqlite
   ORM
   User.objects.all()
   SQL
   SELECT * FROM users_user;
   ```

2. ```sqlite
   ORM
   User.objects.filter(pk=19).values('age')
   SQL
   SELECT age FROM users_user
   WHERE id=19;
   ```

3. ```sqlite
   ORM
   User.objects.values('age')
   SQL
   SELECT age FROM users_user;
   ```

4. ```sqlite
   ORM
   User.objects.filter(age__lte=40).values('id', 'balance')
   SQL
   SELECT id, balance FROM users_user
   WHERE age <= 40;
   ```

5. ```sqlite
   ORM
   User.objects.filter(last_name='김', balance__gte=500).values('first_name')
   SQL
   SELECT first_name FROM users_user
   WHERE last_name='김' AND balance >= 500;
   ```

6. ```sqlite
   ORM
   User.objects.filter(first_name__endswith='수', country='경기도').values('balance')
   SQL
   SELECT balance FROM users_user
   WHERE first_name LIKE '%수' AND country='경기도';
   ```

7. ```sqlite
   ORM
   User.objects.filter(Q(balance__gte=2000)|Q(age__lte=40)).count()
   SQL
   SELECT COUNT(*) FROM users_user
   WHERE balance >= 2000 OR age <= 40;
   ```

8. ```sqlite
   ORM
   User.objects.filter(phone__startswith='010').count()
   SQL
   SELECT COUNT(*) FROM users_user
   WHERE phone LIKE '010%';
   ```

9. ```sqlite
   ORM
   User.objects.filter(first_name='옥자', last_name='김').update(country='경기도')
   
   User.objects.filter(first_name='옥자', last_name='김').values('country')
   SQL
   UPDATE users_user SET country='경기도'
   WHERE first_name='옥자' AND lsat_name='김';
   
   SELECT country FROM users_user
   WHERE first_name='옥자' AND last_name='김';
   ```

10. ```sqlite
    ORM
    User.objects.filter(first_name='진호', last_name='백').delete()
    
    User.objects.filter(first_name='진호', last_name='백').values()
    SQL
    DELETE FROM users_user
    WHERE first_name='진호' AND last_name='백';
    
    SELECT * FROM users_user
    WHERE first_name='진호' AND last_name='백';
    ```

11. ```sqlite
    ORM
    User.objects.order_by('-balance').values('first_name', 'last_name', 'balance')[:4]
    SQL
    SELECT first_name, last_name, balance FROM users_user
    ORDER BY balance DESC
    LIMIT 4;
    ```

12. ```sqlite
    ORM
    User.objects.filter(phone__contains='123', age__lt=30).values()
    SQL
    SELECT * FROM users_user
    WHERE phone LIKE '%123%' AND age < 30;
    ```

13. ```sqlite
    ORM
    User.objects.filter(phone__startswith='010').values('country').distinct()
    SQL
    SELECT DISTINCT country FROM users_user
    WHERE phone LIKE '010%';
    ```

14. ```sqlite
    ORM
    User.objects.aggregate(Avg('age'))
    SQL
    SELECT AVG(age) FROM users_user;
    ```

15. ```sqlite
    ORM
    User.objects.filter(last_name='박').aggregate(park_avg=Avg('balance'))
    SQL
    SELECT AVG(balance) FROM users_user
    WHERE last_name='박';
    ```

16. ```sqlite
    ORM
    User.objects.filter(country='경상북도').aggregate(gb_mxbal=Max('balance'))
    SQL
    SELECT MAX(balance) FROM users_user
    WHERE country='경상북도';
    ```

17. ```sqlite
    ORM
    User.objects.filter(country='제주특별자치도').order_by('-balance').values('first_name')[:1]
    SQL
    SELECT first_name FROM users_user
    WHERE country='제주특별자치도'
    LIMIT 1;
    ```

