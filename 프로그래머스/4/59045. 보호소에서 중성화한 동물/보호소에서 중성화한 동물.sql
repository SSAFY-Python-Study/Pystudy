-- 처음엔 안했는데, 여기 와서 중성화를 한 동물 찾기
select animal_id, animal_type, name
from animal_outs
where 
    (SEX_UPON_outcome like 'Spayed%' or SEX_UPON_outcome like 'Neutered%')
    and animal_id in 
    (SELECT i.animal_id
    from animal_ins as i
    left join animal_outs as o
    on i.animal_id = o.animal_id
    where i.sex_upon_intake != o.sex_upon_outcome)
order by animal_id;