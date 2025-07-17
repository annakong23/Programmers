(select date_format(sales_date, '%Y-%m-%d') SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
from online_sale
where left(sales_date,7)='2022-03')
UNION ALL
(select SALES_DATE, PRODUCT_ID, null USER_ID, SALES_AMOUNT
from offline_sale
where left(sales_date,7)='2022-03')
order by sales_date, product_id, user_id