select concat('/home/grep/src/',board_id,'/',file_id,file_name,file_ext) FILE_PATH 
from used_goods_file
where board_id=(select board_id from used_goods_board order by views desc limit 1)
order by file_id desc

# select *
# from used_goods_file
# where file_id='IMG_000011'

# select board_id from used_goods_board order by views desc limit 1

# select distinct board_id
# from used_goods_file
# where board_id=(select board_id from used_goods_board order by views desc limit 1)
