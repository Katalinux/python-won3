select count(*) from students;

select count(*) from students where l_name ='Popescu';

select count(*) from students where cl_id = (select id from classes where cl_nr = 10 and cl_letter='C');