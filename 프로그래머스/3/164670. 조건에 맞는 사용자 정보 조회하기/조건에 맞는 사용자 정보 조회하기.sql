select USER_ID, NICKNAME, concat(city,' ',street_address1,' ',street_address2) 전체주소, concat(left(TLNO,3),'-',substring(TLNO,4,4),'-',right(TLNO,4)) 전화번호
from used_goods_user
where user_id in (select writer_id 
                  from used_goods_board 
                  group by writer_id 
                  having count(*)>=3)
order by user_id desc