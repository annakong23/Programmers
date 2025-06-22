select NAME, DATETIME
from animal_ins
where animal_id not in (select animal_id from animal_outs)
order by DATETIME
limit 3