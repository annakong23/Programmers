select p.PRODUCT_ID, p.PRODUCT_NAME, sum(o.amount)*p.price TOTAL_SALES
from food_order o inner join food_product p on o.product_id=p.product_id
where o.produce_date like '2022-05%'
group by o.product_id
order by total_sales desc, p.product_id asc
