select ANIMAL_ID, i.NAME
from animal_ins i join animal_outs o using(animal_id)
order by o.datetime - i.datetime desc
limit 2