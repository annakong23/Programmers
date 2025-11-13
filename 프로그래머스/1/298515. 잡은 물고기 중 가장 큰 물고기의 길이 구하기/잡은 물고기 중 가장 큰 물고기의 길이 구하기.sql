select concat(length, 'cm') MAX_LENGTH
from fish_info
order by length desc
limit 1