from functions.general import get_con, set_con
import psycopg2

def connect():
    con = get_con()
    if con is None:
        con = set_con(create_connection())
        return con
    else:
        return con

def create_connection():
    # connect to the database
    con = psycopg2.connect(
        host='drona.db.elephantsql.com',
        database='uyhjjdbf',
        user='uyhjjdbf',
        password='uh5uijULaszUO2VkCvrLOTi9rkeAPZ0z'
    )
    set_con(con)
    return get_con()

def execute_dql_query(query):
    # create a cursor
    con = connect()
    cur = con.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows # gonna return array of tubles

def execute_dml_query(query):
    # create a cursor
    con = connect()
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    return cur.rowcount # gonna return the affected row count

