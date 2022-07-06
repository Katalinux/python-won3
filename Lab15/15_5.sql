update student set school_type = 'High School' where class_nr >= 9;
update student set school_type = 'Gymnasium' where class_nr <= 8;

select * from student where school_type = 'High School';
select * from student where school_type = 'Gymnasium';
