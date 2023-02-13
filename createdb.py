import psycopg2
from config_database import host, user, password, db_name, port

class CreateDB:
    def connect_db(self, function):
        try:
            # connect to exist database
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                dbname=db_name,
                port=port
            )

            connection.autocommit = True

            function(connection)

        except Exception as exc:
            print("[INFO] Error while working with PostgreSQL")
            print(exc)

        else:
            if connection:
                connection.close()
                print("[INFO] PostgreSQL connection closed")



    def create_table_results(self, connection):
        with connection.cursor() as cursor:
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS results (
                id_result int PRIMARY KEY,
                result real NOT NULL
                )"""
            )
        print("[INFO] Table 'results' created")


    def create_table_operations(self, connection):
        with connection.cursor() as cursor:
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS operations (
                id_operation int PRIMARY KEY,
                operand_1 real NOT NULL,
                operation text NOT NULL,
                operand_2 real NOT NULL,
                fk_operation_result int NOT NULL,
                FOREIGN KEY (fk_operation_result) REFERENCES results (id_result)
                )"""
            )
        print("[INFO] Table 'operations' created")


    def results_table(self):
        return self.connect_db(self.create_table_results)

    def operations_table(self):
        return self.connect_db(self.create_table_operations)
