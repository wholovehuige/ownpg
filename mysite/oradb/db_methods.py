import cx_Oracle

def oracle_connection(host,port,db_name,username,password):
    try:
        tns = cx_Oracle.makedsn(host, port, db_name)
        conn = cx_Oracle.connect(username, password, tns)
        return conn
    except(Exception):
        print(Exception)
        return False


def mysql_connection():
    pass

def postgresql_connection():
    pass