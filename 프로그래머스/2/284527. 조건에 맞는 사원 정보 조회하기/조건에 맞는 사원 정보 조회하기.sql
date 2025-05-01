select sum(g.score) SCORE, g.EMP_NO, e.EMP_NAME, e.POSITION, e.EMAIL
from hr_employees e inner join hr_grade g on e.emp_no=g.emp_no
where g.year='2022'
group by g.emp_no
order by SCORE desc
limit 1