
(select name as results from movierating
join users using(user_id)
group by user_id
order by  count(rating) desc, name
limit 1)
union all
(select title from movierating
join movies using(movie_id)
where year(created_at)=2020 and month(created_at)=02
group by title
order by avg(rating) desc,title
limit 1)

--but not just UNION because it will not have the same result if name and title have the same value
-- if title = name; union return
| results |
| rebeca  |
| rebeca  |
-- and union all return
| results |
| rebeca  |