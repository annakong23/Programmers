select left(product_code,2) CATEGORY, count(*) PRODUCTS
from product
group by category
order by category