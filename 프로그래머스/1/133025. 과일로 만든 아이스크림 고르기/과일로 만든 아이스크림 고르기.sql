-- 코드를 입력하세요
SELECT i.FLAVOR
from first_half f LEFT OUTER JOIN ICECREAM_INFO i on f.FLAVOR=i.FLAVOR
where f.total_order > 3000 and i.ingredient_type='fruit_based'
order by f.total_order desc