select f.ID, n.FISH_NAME, f.length LENGTH
from fish_info f inner join fish_name_info n on f.fish_type=n.fish_type
where (f.fish_type, f.length) in (select fish_type, max(length) from fish_info group by fish_type)
order by f.id