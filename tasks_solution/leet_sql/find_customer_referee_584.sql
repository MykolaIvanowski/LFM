select name from customer
where referee_id <> 2 or referee_id is null

-- this sql in not pass the tests on leet (have different result)
select name from customer
where referee_id != 2 or referee_id is null
