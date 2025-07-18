# select CATEGORY, PRICE MAX_PRICE, PRODUCT_NAME
# from food_product
# where category in ('과자', '국', '김치', '식용유') 
# group by category
# having max(price)
# order by price desc

# select * from food_product
# where category in ('과자', '국', '김치', '식용유') 
# order by category



select CATEGORY, PRICE MAX_PRICE, PRODUCT_NAME
from food_product
where (category,price) in (select category, max(price)
                               from food_product
                               where category in ('과자','국','김치','식용유')
                               group by category)
order by price desc                       






