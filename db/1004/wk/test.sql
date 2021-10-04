CREATE TABLE countries (
  room_num TEXT,
  check_in TEXT,
  check_out TEXT,
  grad TEXT,
  price INTIGER
);

INSERT INTO countries
VALUES ('B203', '2019-12-31', '2020-01-03', 'suite', 900);

INSERT INTO countries
VALUES ('1102', '2020-01-04', '2020-01-08', 'suite', 850);

INSERT INTO countries
VALUES ('303', '2020-01-01', '2020-01-03', 'deluxe', 500);

INSERT INTO countries
VALUES ('807', '2020-01-04', '2020-01-07', 'superior', 300);

SELECT * FROM countries;


ALTER TABLE countries
RENAME TO hotels;

SELECT * FROM hotels;

SELECT room_num, price FROM hotels
ORDER BY price DESC
LIMIT 2;

SELECT grad, COUNT(grad) FROM hotels
GROUP BY grad;

ALTER TABLE hotels
RENAME COLUMN grad TO grade;

SELECT grade, COUNT(grade) AS cnt_grade FROM hotels
GROUP BY grade;

SELECT * FROM hotels
WHERE room_num LIKE 'B%' OR grade='deluxe';

SELECT room_num, price FROM hotels
WHERE room_num NOT LIKE 'B%' AND check_in='2020-01-04'
ORDER BY price;