select m.MEMBER_NAME, r.REVIEW_TEXT, date_format(r.REVIEW_DATE,'%Y-%m-%d') REVIEW_DATE
from rest_review r join member_profile m on r.member_id=m.member_id
where r.member_id=(select member_id
                 from rest_review
                 group by member_id
                 order by count(*) desc
                 limit 1)
order by r.review_date, r.review_text

# select member_id
# from rest_review
# group by member_id
# order by count(*) desc
# limit 1