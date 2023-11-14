from sqlalchemy import create_engine
from duomenys import get_data
import pandas as pd
import psycopg2
from psycopg2 import sql

def connect_db():
    conn_params = {
        'database':'postgres',
        'dbname': 'Profes_ligos',
        'user': 'postgres',
        'password': '23duomenubaze23',
        'host': 'localhost'
    }
    return conn_params
def creat_database(dbname,user,password,host, port,new_dbname,**kwargs):
    conn_params={
        "database":dbname,
        "user":user,
        "password":password,
        "host":host,
        "port":port
    }
    try:
        connection=psycopg2.connect(**conn_params)
        connection.autocommit=True
        cursor=connection.cursor()
        cursor.execute(sql.SQL('CREATE DATABASE {}').format(sql.Identifier(new_dbname)))
        print(f'database {new_dbname} created secsesfuli')
        cursor.close()
        connection.close()
    except psycopg2.Error as e:
        print(f'An Error occured while creating the database{e}')
# creat_database("postgres","postgres",'23duomenubaze23','localhost',5432,'Profes_ligos') ##funkcijos kvietimas
def write_to_database(df, table_name, db_params):
    # Sukuriame sujungimą su duomenu baze
    engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["database"]}')

    # Irasome dataframe su duomenimis i lentele
    df.to_sql(table_name, engine, index=False, if_exists='replace')  # cia jeigu duomenys lenteleje jau egzistuoja, pakeiciame juos naujais, jeigu norime papildyti vietoje replace reikia irasyti append

    # uzdarome duomenu bazes konektoriu
    engine.dispose()

def read_from_database(table_name, db_params):
    # Create a database connection
    engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["database"]}')

    # SQL query to select data from the table
    query = f'SELECT * FROM "{table_name}"'

    # Read data from the database into a DataFrame
    df_read = pd.read_sql(query, engine)

    # Close the database connection
    engine.dispose()

    return df_read

# dataframe su asmens duomenimis
df = get_data()

# prisijungimo prie duomenu bazes parametrai
db_params = {
    'host': 'localhost',
    'port': '5432',
    'user': 'postgres',
    'password': '23duomenubaze23',
    'database': 'Profes_ligos',
}

table_name = 'Asmenys'  # Lenteles i kuria rasome/skaitome pavadinimas

# Irasome dataframe su duomenimis i lentele
write_to_database(df, table_name, db_params)

# Nuskaitome duomenis is DB į df_read Pandas dataframe
df_read = read_from_database(table_name, db_params)

print(df_read)