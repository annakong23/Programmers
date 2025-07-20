# 1)
select a.FLAVOR
from
((select *
from first_half)
union all
(select *
from july)) as a
group by flavor
order by sum(total_order) desc
limit 3;

# 2)
select j.flavor
from first_half h
join
(select flavor, sum(total_order) total_order
from july
group by flavor) j on h.flavor=j.flavor
order by (h.total_order+j.total_order) desc
limit 3;

# 3)
SELECT flavor
FROM first_half f
LEFT JOIN july j 
USING (flavor)
GROUP BY flavor
ORDER BY (f.total_order + SUM(j.total_order)) DESC
LIMIT 3;