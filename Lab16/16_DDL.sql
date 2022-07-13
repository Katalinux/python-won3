create table classes (
id serial primary key,
cl_nr smallint NOT NULL,
cl_letter varchar(1) NOT NULL,
profile varchar(20),
master varchar(25)
);

create table students (
id serial primary key,
l_name varchar(20),
f_name varchar(20),
b_date date NOT NULL,
cl_id smallint NOT NULL,
foreign key (cl_id) references classes(id)
);

create table disciplines (
id serial primary key,
discipline varchar(20) NOT NULL
);

create table grades (
id serial primary key,
std_id smallint NOT NULL,
dis_id smallint NOT NULL,
grade decimal NOT NULL,
c_date date default current_date,
foreign key (std_id) references students(id),
foreign key (dis_id) references disciplines(id)
);