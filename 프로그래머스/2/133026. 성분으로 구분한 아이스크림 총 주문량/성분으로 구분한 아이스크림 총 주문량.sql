select i.INGREDIENT_TYPE, sum(f.total_order) TOTAL_ORDER
from first_half f, icecream_info i 
where f.flavor=i.flavor
group by i.ingredient_type
order by total_order
