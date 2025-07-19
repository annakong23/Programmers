set @HOUR = -1;
select (@HOUR := @HOUR + 1) HOUR,(select count(hour(datetime)) 
from animal_outs
where hour(datetime)=@hour) COUNT
from animal_outs
where @HOUR < 23
