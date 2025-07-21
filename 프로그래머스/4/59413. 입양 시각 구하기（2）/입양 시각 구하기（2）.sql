# set @HOUR = -1;
# select (@HOUR := @HOUR+1) HOUR, (select count(*) from animal_outs where hour(datetime)=@HOUR) COUNT
# from animal_outs
# where @hour<23
# order by hour;

# select hour(datetime) HOUR, count(animal_id) COUNT
# from animal_outs
# group by hour
# order by hour
set @HOUR= -1;
select (@HOUR := @HOUR+1), (select count(animal_id) from animal_outs where hour(datetime)=@hour) COUNT
from animal_outs
where @HOUR < 23
order by @hour;









