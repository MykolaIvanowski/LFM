
select u.name, ifnull(sum(distance),0) as travelled_distance from users u
left join rides r on u.id=r.user_id
group by u.name, u.id
order by 2 desc, name asc