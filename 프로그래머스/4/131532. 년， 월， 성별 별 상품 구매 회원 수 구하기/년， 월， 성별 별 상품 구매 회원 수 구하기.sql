select year(s.sales_date) YEAR, month(s.sales_date) MONTH, u.GENDER, count(distinct s.user_id) USERS
from online_sale s join user_info u using(user_id)
where gender is not null
group by year, month, u.gender
order by year, month, u.gender