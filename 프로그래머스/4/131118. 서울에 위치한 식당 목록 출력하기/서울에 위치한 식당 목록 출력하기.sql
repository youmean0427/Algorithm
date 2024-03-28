
SELECT B.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, SCORE
FROM (SELECT REST_ID, ROUND(AVG(REVIEW_SCORE), 2) AS SCORE
FROM REST_REVIEW
GROUP BY REST_ID) AS B RIGHT JOIN REST_INFO ON B.REST_ID = REST_INFO.REST_ID
WHERE (ADDRESS LIKE "서울특별시%" OR ADDRESS LIKE  "서울시%") AND ISNULL(SCORE) = FALSE
ORDER BY SCORE DESC, FAVORITES DESC