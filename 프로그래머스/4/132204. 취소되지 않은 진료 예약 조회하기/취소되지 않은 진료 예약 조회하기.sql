select a.APNT_NO, p.PT_NAME,p.PT_NO, a.MCDP_CD, d.DR_NAME,a.APNT_YMD
from appointment a 
join patient p on a.pt_no=p.pt_no
join doctor d on d.dr_id=a.mddr_id
where a.mcdp_cd='CS' and a.APNT_CNCL_YN='N' and left(a.apnt_ymd,10)='2022-04-13'
order by a.apnt_ymd