select user_id, name, mail from users
where mail REGEXP '^[A-Za-z][A-Za-z0-9._-]*@leetcode\\.com$';


--other solution
SELECT *
FROM Users
WHERE mail REGEXP '^[a-zA-Z][a-zA-Z0-9_\.\-]*@leetcode(\\?com)?\\.com$';