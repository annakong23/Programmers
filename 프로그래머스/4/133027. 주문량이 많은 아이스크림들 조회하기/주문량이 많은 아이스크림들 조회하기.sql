select a.FLAVOR
from
((select *
from first_half)
union all
(select *
from july)) as a
group by flavor
order by sum(total_order) desc
limit 3
# select *
# from first_half h full outer join
# (select flavor, sum(total_order)
# from july
# group by flavor) j on h.flavor=j.flavor
