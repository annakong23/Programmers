select FLOOR(price/10000)*10000 PRICE_GROUP, count(*) PRODUCTS
from product
group by price_group
order by price_group



# select PRICE_GROUP, PRODUCTS
# from product
# group by case 
# when price < 10000 then '0'
# when price between 10000 and 19999 then '10000'
# when price between 20000 and 29999 then '20000'
# when price between 30000 and 39999 then '30000'
# when price between 40000 and 49999 then '40000'
# when price between 50000 and 59999 then '50000'
# when price between 60000 and 69999 then '60000'
# when price between 70000 and 79999 then '70000'
# else '80000'
# as PRICE_GROUP

