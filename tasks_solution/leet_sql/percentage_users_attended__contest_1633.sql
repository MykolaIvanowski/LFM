select contest_id,
 round(
    count(contest_id)*100/(select count(*) from users ),2) as percentage
    from users
join register using(user_id)
group by contest_id
order by 2 desc, contest_id asc