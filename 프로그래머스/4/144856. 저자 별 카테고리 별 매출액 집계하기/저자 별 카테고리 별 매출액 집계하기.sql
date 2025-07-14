select a.AUTHOR_ID, a.AUTHOR_NAME, bs.CATEGORY, bs.TOTAL_SALES
from author a join 
(
select b.category, b.author_id, (sum(s.sales * b.price)) TOTAL_SALES
from book b join book_sales s on b.book_id=s.book_id
where left(s.sales_date,7)='2022-01'
group by b.author_id, b.category
) bs on a.author_id=bs.author_id
order by a.author_id asc, bs.category desc