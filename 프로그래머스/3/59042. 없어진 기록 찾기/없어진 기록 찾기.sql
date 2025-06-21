select o.ANIMAL_ID, o.NAME
from animal_ins i right outer join animal_outs o on i.animal_id=o.animal_id
where i.datetime is null
order by o.animal_id