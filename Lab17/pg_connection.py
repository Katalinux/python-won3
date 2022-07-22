import psycopg2


def pg_conn():
    try:
        return psycopg2.connect(
            host="localhost",
            database="PYT_WON3",
            user="postgres",
            password="kata")
    except psycopg2.DatabaseError as err:
        print(err)
