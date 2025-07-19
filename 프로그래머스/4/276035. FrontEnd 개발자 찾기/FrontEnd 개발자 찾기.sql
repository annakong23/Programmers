select distinct d.ID, d.EMAIL, d.FIRST_NAME, d.LAST_NAME
from developers d join skillcodes s on d.skill_code & s.code
where s.category='Front End'
order by d.id asc