select CAR_ID, case when max('2022-10-16' between start_date and end_date) then '대여중' else '대여 가능' end AVAILABILITY
from car_rental_company_rental_history
group by car_id
order by car_id desc