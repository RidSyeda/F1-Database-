def create_Sqlite_connection(location_path, database_name):
    import sqlite3
    global connection
    connection = None
    location=location_path
    F1DB= database_name
    conn=location+F1DB
    print (conn)
    connection = sqlite3.connect(conn)
    print('Database is created.')
    connection.commit()
    print('Changes is saved.')
    return connection

def displaydbtable(query_string, connection):
    import pandas as pd
    query_str = query_string
    print(query_str)
    dataframe = pd.read_sql(query_str, connection)
    return dataframe