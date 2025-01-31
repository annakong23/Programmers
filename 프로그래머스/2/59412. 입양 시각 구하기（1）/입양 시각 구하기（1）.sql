-- 코드를 입력하세요
SELECT date_format(datetime, '%H') HOUR, count(*) COUNT
from animal_outs
group by HOUR #date_format(datetime, '%H')
having HOUR >= 9 and HOUR<20
order by HOUR

