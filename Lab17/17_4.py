import psycopg2
import pg_connection as pg

conn = pg.pg_conn()
last_name = input('Last Name: ')
first_name = input('First Name: ')

with conn:
    c = conn.cursor()
    try:
        c.execute("""select * from students where l_name = %s and f_name = %s;""", (last_name, first_name))
        results = c.fetchone()
        if results:
            c.execute("""select (select discipline from disciplines d where d.id = g.dis_id), grade, c_date from
             grades g where std_id = %s order by grade desc;""", str(results[0]))
            details = c.fetchall()
            c.execute("""select cl_nr, cl_letter from classes where id =%s""", str(results[-1]))
            cls_nr = c.fetchone()
            print(f'\n{last_name} {first_name} | Class: {cls_nr[0]}{cls_nr[1]}\nGrades:')
            for d in details:
                print(f'{d[0]}: {d[1]} | Date: {d[2]}')
        else:
            print(f'No results for: {last_name} {first_name}')
    except psycopg2.OperationalError as e:
        print('DB error:', e)
