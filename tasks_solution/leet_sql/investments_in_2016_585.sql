
select round(sum(a.tiv_2016),2) as tiv_2016 from insurance a
where a.tiv_2015 in (
    select insurance.tiv_2015
    from insurance
    where a.pid <> insurance.pid
    )
and (a.lon, a.lat) not in (
    select insurance.lon, insurance.lat
    from insurance
    where a.pid <> insurance.pid
    )