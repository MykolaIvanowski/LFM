select ra.requester_id as id , sum(ra.num) as num from (
    select  requester_id , count(requester_id) as num
    from requestaccepted
    group by requester_id
    union all
    select accepter_id, count(accepter_id)
    from requestaccepted
    group by accepter_id
    ) as ra
group by ra.requester_id
order by 2 desc
limit 1


-- different way solutions

--#Solution 1:
with base as(select requester_id id from RequestAccepted
union all
select accepter_id id from RequestAccepted)


select id, count(*) num  from base group by 1 order by 2 desc limit 1