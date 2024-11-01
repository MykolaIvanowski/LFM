
select e.name from employee e
join employee e1 on e.id = e1.managerid
group by e1.managerid
having count(e1.managerid) > 4


--another way with sub query