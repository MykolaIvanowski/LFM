select name, sum(amount) as balance from users
right join transactions using(account)
group by name
having sum(amount) > 10000