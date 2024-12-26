select user_id,
        round(coalesce(sum(if(action='confirmed',1,0))/count(action),0),2) as confirmation_rate
from signups
left join confirmations using(user_id)
group by 1



--The confirmation rate of a user is the number of 'confirmed' messages divided
--by the total number of requested confirmation messages. The confirmation rate of a user
--that did not request any confirmation messages is 0. Round the confirmation rate
--to two decimal places.