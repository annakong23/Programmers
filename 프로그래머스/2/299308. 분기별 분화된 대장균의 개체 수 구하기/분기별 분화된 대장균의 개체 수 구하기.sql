# select concat(quarter(differentiation_date),'Q') QUARTER, count(id) ECOLI_COUNT
# from ecoli_data
# group by quarter
# order by quarter



select concat(quarter(differentiation_date),'Q') QUARTER, count(*) ECOLI_COUNT
from ecoli_data
group by QUARTER
order by QUARTER








