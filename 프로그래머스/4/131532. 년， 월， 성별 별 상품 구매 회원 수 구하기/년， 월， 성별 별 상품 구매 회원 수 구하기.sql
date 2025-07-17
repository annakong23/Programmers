select year(s.sales_date) YEAR, month(s.sales_date) MONTH, u.GENDER, count(distinct u.user_id) USERS
from online_sale s join user_info u on s.user_id=u.user_id
where u.gender is not null
group by year, month, gender
order by year, month, gender