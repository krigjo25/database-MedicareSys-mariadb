#   Python Libraries
from os import getenv
from typing import Any, Dict, List

#   Third party libraries
import mariadb
from dotenv import load_dotenv

load_dotenv()


class MariaDB():

    '''         mariaDB

        Connects to the preferably used database from
        mariaDB. with Commands, such as SELECT, INSERT,
        UPDATE, CREATE DATABASE, CREATE TABLE
                
        the function also calls a procedure and a function.
    '''

    def __init__(self):

        try:
            #   Initializing the database connection
            self.conn = mariadb.connect(
                                        host = getenv('H0ST'), 
                                        user = getenv('MASTER'), 
                                        port = int(getenv('PORT')), 
                                        password = getenv('PASSWORD'),
                                        database = getenv('database'))
            
            #   Creating a cursor to execute the statements
            self.cur = self.conn.cursor()

        except mariadb.Error as e:
            print(f"Error connecting to the database: \n {e}")
            exit(1)

        return
    def close_connection (self) -> None: self.conn.close()

    def fetch_records (self, database: str, query: str) -> List[Dict[str, Any]]:

        self.conn.database = database

        #  Execute the query.
        self.cur.execute(query)


        sql = self.cur.fetchall()

        sqlData = [i for i in sql]
        return sqlData

    def row_count(self, database: str, query: str) -> int:

        #   Database selection
        self.conn.database = database

        #   Executes the query and retrieve the rows
        self.cur.execute(query)

        #   Fetch the cursor
        self.cur.fetchall()

        return self.cur.rowcount

    def upsert_table (self, database: str, query: str) -> None:

        #   Database selection
        self.conn.database = database

        self.database = database

        self.cur.execute(query)
        self.close_connection()

        return

    def call_procedure (self, database: str, query: str):

        #   Database Connection 
        self.conn.database = database

        #   calling a procedure
        self.cur.callproc(f'{query}')

        return

    def fetch_patient_records(self): return