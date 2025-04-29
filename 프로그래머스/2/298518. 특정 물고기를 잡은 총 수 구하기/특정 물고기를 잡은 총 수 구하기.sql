select count(*) FISH_COUNT
from fish_info i left outer join fish_name_info n on i.fish_type=n.fish_type
where n.fish_name='BASS' or n.fish_name='SNAPPER'

# select count(*) FISH_COUNT
# from fish_info
# where fish_type=0 or fish_type=1
