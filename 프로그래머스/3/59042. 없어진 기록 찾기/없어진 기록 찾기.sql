-- 입양을 갔는데out, 보호소에 들어온in 기록이 없다?
SELECT o.animal_id, o.name
from animal_outs o
left join animal_ins i
on o.animal_id = i.animal_id
where i.animal_id is null
order by o.animal_id;