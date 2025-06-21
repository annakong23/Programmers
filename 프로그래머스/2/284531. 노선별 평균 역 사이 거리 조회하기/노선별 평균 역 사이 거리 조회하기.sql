select ROUTE, concat(round(sum(D_BETWEEN_DIST),1),'km') TOTAL_DISTANCE, concat(round(avg(D_BETWEEN_DIST),2),'km') AVERAGE_DISTANCE
from subway_distance
group by route
order by (TOTAL_DISTANCE-'km') desc