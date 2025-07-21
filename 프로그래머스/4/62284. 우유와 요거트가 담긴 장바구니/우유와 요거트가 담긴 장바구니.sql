select CART_ID
from cart_products a join cart_products b using(cart_id)
where a.name='Milk' and b.name='Yogurt'
order by cart_id