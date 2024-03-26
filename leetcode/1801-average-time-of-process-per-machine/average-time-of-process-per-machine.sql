# Write your MySQL query statement below
with start_activity as (
    select * 
    from activity
    where activity_type = 'start' 
),
end_activity as (
    select * 
    from activity
    where activity_type = 'end' 
),
joined_activities as (
    select s.machine_id, e.timestamp - s.timestamp as processing_time
    from start_activity s
    inner join end_activity e 
        on e.machine_id = s.machine_id and e.process_id = s.process_id 
)
select machine_id, round(avg(processing_time), 3) as processing_time
from joined_activities
group by machine_id
;

