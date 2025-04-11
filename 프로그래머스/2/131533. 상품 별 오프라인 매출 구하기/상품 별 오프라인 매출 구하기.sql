-- 코드를 입력하세요
SELECT p.PRODUCT_CODE, sum(p.price*s.sales_amount) SALES
from product p, offline_sale s
where p.product_id = s.product_id
group by p.product_code
order by SALES desc, p.product_code asc
