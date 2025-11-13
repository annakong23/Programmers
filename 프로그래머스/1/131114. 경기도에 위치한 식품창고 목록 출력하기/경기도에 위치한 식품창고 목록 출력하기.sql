# SELECT warehouse_id, warehouse_name, address, ifnull(freezer_yn, 'N')
# from food_warehouse
# where warehouse_name like '%경기%'
# order by warehouse_id


select WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, ifnull(freezer_yn,'N') FREEZER_YN
from food_warehouse
where address like '경기도%'
order by warehouse_id









