-- 코드를 작성해주세요
select concat(quarter(differentiation_date),'Q') QUARTER, count(*) ECOLI_COUNT
from ecoli_data
group by quarter