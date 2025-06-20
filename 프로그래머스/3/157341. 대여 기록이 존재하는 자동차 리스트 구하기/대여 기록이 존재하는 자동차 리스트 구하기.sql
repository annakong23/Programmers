select distinct c.CAR_ID
from CAR_RENTAL_COMPANY_CAR c join CAR_RENTAL_COMPANY_RENTAL_HISTORY h on c.car_id=h.car_id
where c.car_type='세단' and substring(h.start_date, 6, 2)='10'
order by c.car_id desc