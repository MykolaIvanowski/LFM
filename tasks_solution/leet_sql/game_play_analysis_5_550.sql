-- Write your MySQL query statement below

select round(count(distinct activity.player_id)/count(distinct min_t.player_id), 2) as fraction
from (
    select player_id, min(event_date) as event_date
    from activity
    group by player_id
    ) as min_t
left join activity
on DATEDIFF(activity.event_date, min_t.event_date) = 1
and min_t.player_id = activity.player_id
