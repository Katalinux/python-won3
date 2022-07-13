insert into classes (cl_nr, cl_letter, profile, master) values ('12', 'A', 'Informatics', 'prof. Dinu Georgescu');
insert into classes (cl_nr, cl_letter, profile, master) values ('12', 'B', 'Social Science', 'prof. Ioana Radu');
insert into classes (cl_nr, cl_letter, profile, master) values ('12', 'C', 'Informatics', 'prof. Nae Popescu');


insert into students (l_name, f_name, b_date, cl_id) values ('Popescu', 'Ana', '2006-03-05', '1');
insert into students (l_name, f_name, b_date, cl_id) values ('Fieraru', 'George', '2006-05-21', '3');
insert into students (l_name, f_name, b_date, cl_id) values ('Vasilescu', 'Cosmin', '2006-09-15', '3');
insert into students (l_name, f_name, b_date, cl_id) values ('Zeriu', 'Marius', '2006-04-06', '1');


insert into disciplines (discipline) values ('Mathematics');
insert into disciplines (discipline) values ('Physics');
insert into disciplines (discipline) values ('Informatics');
insert into disciplines (discipline) values ('Sociology');
insert into disciplines (discipline) values ('Linguistics');


insert into grades(std_id, dis_id, grade) values ('1', '1', '9.4');
insert into grades(std_id, dis_id, grade) values ('1', '3', '8.2');
insert into grades(std_id, dis_id, grade) values ('2', '2', '7.0');
insert into grades(std_id, dis_id, grade) values ('2', '4', '7.8');
insert into grades(std_id, dis_id, grade) values ('3', '4', '6.4');
insert into grades(std_id, dis_id, grade) values ('3', '5', '8.4');
insert into grades(std_id, dis_id, grade) values ('4', '1', '7.8');
insert into grades(std_id, dis_id, grade) values ('4', '1', '9.0');