import psycopg2
from config_database import host, user, password, db_name, port
from sdfgs import insert_result, insert_operation, select_result_id, select_operation, select_result





def paste_new_oper_res(result=None, operand_1=None, operand_2=None, operator=None, id_result=0):
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

        if id_result == 0:
            id_result_new = insert_result(
                connection=connection,
                result=result
            )
        else:
            id_result_new = id_result
        insert_operation(
            connection=connection,
            operand_1=operand_1,
            operator=operator,
            operand_2=operand_2,
            id_result=id_result_new
        )

    except Exception as exc:
        print("[INFO] Error while working with PostgreSQL")
        print(exc)

    else:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")



def check_res_db(result):
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

        id_result = select_result_id(
            connection=connection,
            result=result
        )
        if id_result != 0:
            print("[INFO] Result is already in database")

    except Exception as exc:
        print("[INFO] Error while working with PostgreSQL")
        print(exc)

    else:
        if connection:
            connection.close()
            # print("[INFO] PostgreSQL connection closed")
            return id_result

def check_operation_db(operand_1, operand_2, operation):
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

        fk_operation_result = select_operation(
            connection=connection,
            operand_1=operand_1,
            operand_2=operand_2,
            operation=operation,
        )
        if fk_operation_result:
            result = select_result(
                connection=connection,
                fk_operation_result=fk_operation_result,
            )
            if result:
                return result
            else:
                return False

    except Exception as exc:
        print("[INFO] Error while working with PostgreSQL")
        print(exc)

    else:
        if connection:
            connection.close()
            # print("[INFO] PostgreSQL connection closed")


def get_table_data_db():
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

        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT o.operand_1, o.operand_2, o.operation, r.result 
                FROM operations o JOIN results r 
                ON o.fk_operation_result = r.id_result"""
            )
            data_table = cursor.fetchall()

    except Exception as exc:
        print("[INFO] Error while working with PostgreSQL")
        print(exc)

    else:
        if connection:
            connection.close()
            # print("[INFO] PostgreSQL connection closed")
            return data_table

