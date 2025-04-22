-- 코드를 입력하세요
SELECT p.product_code, p.price*sum(sales_amount) as price
from product p
join offline_sale o
on p.product_id = o.product_id
group by p.product_code
order by price desc, product_code asc;