set @HOUR = -1;
select (@HOUR := @HOUR+1) HOUR, (select count(*) from animal_outs where hour(datetime)=@HOUR) COUNT
from animal_outs
where @hour<23
order by hour;

# select hour(datetime) HOUR, count(animal_id) COUNT
# from animal_outs
# group by hour
# order by hour