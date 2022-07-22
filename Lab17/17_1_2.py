import psycopg2
import pg_connection as pg

conn = pg.pg_conn()

with conn:
    c = conn.cursor()
    try:
        c.execute('select l_name as \"Nume\", f_name as \"Prenume\", (select concat(c.cl_nr, c.cl_letter) '
                  'from classes c where s.cl_id = c.id) as \"Clasa\" from students s order by s.l_name;')
        results = c.fetchall()
        header = ('Nume', 'Prenume', 'Clasa')
        with open('students.txt', 'w') as students:
            print(*header)
            students.write(f'{header[0]:<12} {header[1]:<10} {header[2]:>5}\n')
            for r in results:
                print(*r)
                students.write(f'{r[0]:<12} {r[1]:<10} {r[2]:>5}\n')
    except psycopg2.OperationalError as e:
        print('DB error:', e)
