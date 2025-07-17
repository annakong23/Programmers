select i.REST_ID, i.REST_NAME, i.FOOD_TYPE, i.FAVORITES, i.ADDRESS, round(avg(r.review_score),2) SCORE
from rest_review r join rest_info i on r.rest_id=i.rest_id
where left(i.address,2)='서울'
group by i.rest_id
order by score desc