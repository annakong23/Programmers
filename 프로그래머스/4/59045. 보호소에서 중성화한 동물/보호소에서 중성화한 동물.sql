select i.ANIMAL_ID, i.ANIMAL_TYPE, i.NAME
from animal_ins i join animal_outs o on i.animal_id=o.animal_id
where left(i.sex_upon_intake,1)='I' and left(o.sex_upon_outcome,1) in ('N', 'S')
order by animal_id