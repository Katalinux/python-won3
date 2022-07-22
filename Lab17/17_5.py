import psycopg2
import pg_connection as pg


def average_grade(notes: list):
    if len(notes) > 0:
        return round(sum(notes) / len(notes), 1)
    return 0


conn = pg.pg_conn()

with conn:
    try:
        c = conn.cursor()
        c.execute("""delete from student_average""")
        c.execute("""select id from students""")

        for s_id in c.fetchall():
            c.execute("""select grade from grades where std_id=%s""", str(s_id[0]))
            note_lst = []
            for note in c.fetchall():
                note_lst.append(note[0])
            c.execute("""insert into student_average (student_id, average) values(%s, %s)""",
                      (str(s_id[0]), average_grade(note_lst)))

        c.execute("""select concat(s.l_name, ' ',  s.f_name), sa.average from student_average sa 
        join students s on s.id = sa.student_id order by average desc""")

        for item in c.fetchall():
            print(f'{item[0]:<20} {item[1]:>5}')
    except psycopg2.OperationalError as e:
        print(e)
