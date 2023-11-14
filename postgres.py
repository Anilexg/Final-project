from sqlalchemy import create_engine
from duomenys import get_data
import pandas as pd
import psycopg2
from psycopg2 import sql


#Kuriama DB
def creat_database(dbname,user,password,host, port,new_dbname,**kwargs):
    db_params={
        "database":dbname,
        "user":user,
        "password":password,
        "host":host,
        "port":port
    }
    try:
        connection=psycopg2.connect(**db_params)
        connection.autocommit=True
        cursor=connection.cursor()
        cursor.execute(sql.SQL('CREATE DATABASE {}').format(sql.Identifier(new_dbname)))
        print(f'Duomenų bazė pavadinimu  {new_dbname} sukurta sėkmingai')
        cursor.close()
        connection.close()
    except psycopg2.Error as e:
        print(f'Tokia duomenų bazė jau egzistuoja {e}')
# creat_database("postgres","postgres",'23duomenubaze23','localhost',5432,'Profes_ligos') ##funkcijos kvietimas
def write_to_database(df, table_name, db_params):
    # Sukuriame sujungimą su duomenu baze
    engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["database"]}')

    # Įrašome dataframe su duomenimis į lentelę.
    df.to_sql(table_name, engine, index=False, if_exists='replace')  # Jeigu duomenys lentelejė jau egzistuoja, pakeičiame juos naujais

    # Uždarome DB konektorių
    engine.dispose()

def read_from_database(table_name, db_params):
    # Sukuriame sujungimą su DB
    engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["database"]}')

    # SQL užklausa duomenims iš lentelės atrinkti
    query = f'SELECT * FROM "{table_name}"'

    # Duomenų nuskaitymas iš DB į DataFrame
    df_read = pd.read_sql(query, engine)

    # Uždaromas prisijungimas prie DB
    engine.dispose()

    return df_read

# dataframe su asmens duomenimis
df = get_data()

# Prisijungimo prie duomenu bazes parametrai
db_params = {
    'host': 'localhost',
    'port': '5432',
    'user': 'postgres',
    'password': '23duomenubaze23',
    'database': 'Profes_ligos',
}

table_name = 'Asmenys'  # Lenteles i kuria rasome/skaitome pavadinimas

# Įrašome dataframe su duomenimis į lentelę
write_to_database(df, table_name, db_params)

# Nuskaitome duomenis is DB į df_read Pandas dataframe
df_read = read_from_database(table_name, db_params)

print(df_read)