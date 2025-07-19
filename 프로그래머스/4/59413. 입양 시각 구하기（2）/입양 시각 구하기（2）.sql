# set @HOUR = -1;
# select (@HOUR := @HOUR + 1) HOUR,(select count(hour(datetime)) HOUR
# from animal_outs
# where hour(datetime)=@hour) COUNT
# from animal_outs
# where @HOUR < 23;


set @HOUR = -1;
select (@HOUR := @HOUR+1) HOUR, (select count(*) from animal_outs where hour(datetime)=@HOUR) COUNT
from animal_outs
where @hour<23
order by hour;