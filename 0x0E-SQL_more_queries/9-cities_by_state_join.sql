-- a script that lists all cities contained in the database hbtn_0d_usa.
SELECT `id`, `name`, `st.name` FROM `cities`
NATURAL JOIN `states` AS st
ORDER BY `id`;
