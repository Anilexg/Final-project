from sqlalchemy import create_engine
from duomenys import get_data
import pandas as pd

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
    'password': 'Jokubas2017',
    'database': 'Profes_ligos',
}

table_name = 'Asmenys'  # Lenteles i kuria rasome/skaitome pavadinimas

# Irasome dataframe su duomenimis i lentele
write_to_database(df, table_name, db_params)

# Nuskaitome duomenis is DB į df_read Pandas dataframe
df_read = read_from_database(table_name, db_params)

print(df_read)