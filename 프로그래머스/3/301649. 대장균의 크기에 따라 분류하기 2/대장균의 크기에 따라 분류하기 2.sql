# select l.ID, case 
# when l.per<=0.25 then 'CRITICAL'
# when l.per<=0.5 then 'HIGH'
# when l.per<=0.75 then 'MEDIUM'
# else 'LOW' end as COLONY_NAME
# from (select id, percent_rank() over (order by size_of_colony desc) as per
# from ecoli_data) l
# order by id;

# select size_of_colony
# from ecoli_data
# order by size_of_colony desc

# select count(*)
# from ecoli_data

# select id, percent_rank() over (order by size_of_colony)
# from ecoli_data

select ID, case
when percent<=0.25 then 'CRITICAL'
when percent>0.25 and percent<=0.5 then 'HIGH'
when percent>0.5 and percent<=0.75 then 'MEDIUM'
when percent >0.75 then 'LOW'
end 
as COLONY_NAME
from (select id, percent_rank() over (order by size_of_colony desc) as percent from ecoli_data) p
order by id