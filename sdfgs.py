


def insert_result(connection, result):
    """ Внесение в БД в таблицу 'results' значения 'text'."""
    # Вычисление последнего ID
    with connection.cursor() as cursor:
        cursor.execute("""SELECT MAX(id_result) FROM results""")
        id_tup = cursor.fetchone()
        # Проверка отсутствия данных в таблице
        if bool(id_tup[0]) == False:
            id_result = 1
        # Присваивание следующего порядкого ID
        else:
            id_result = id_tup[0] + 1
        # Внесение в таблицу 'results' значения 'result' и присвоение ему 'ID'
        cursor.execute(
            f"""INSERT INTO results
            VALUES({id_result}, {result})"""
        )
    print(f"[INFO] Data added into table results: id - {id_result}, {result}")
    return id_result



def insert_operation(connection, operand_1, operator, operand_2, id_result):
    """ Внесение в БД в таблицу 'operations' значений 'operand_1', 'operand_2', 'operation'."""
    # Вычисление последнего ID
    with connection.cursor() as cursor:
        cursor.execute("""SELECT MAX(id_operation) FROM operations""")
        id_tup = cursor.fetchone()
        # Проверка отсутствия данных в таблице
        if bool(id_tup[0]) == False:
            id_operation = 1
        # Присваивание следующего порядкого ID
        else:
            id_operation = id_tup[0] + 1
        # Внесение в таблицу 'results' значения 'result' и присвоение ему 'ID'
        cursor.execute(
            f"""INSERT INTO operations
            VALUES({id_operation}, {operand_1}, '{operator}', {operand_2}, {id_result})"""
        )
    print(f"[INFO] Data added into table 'operations': id - {id_operation},"
          f"operand_1 - {operand_1}, operand_2 - {operand_2}, operation - {operator}")



def select_result_id(connection, result):
    """ Поиск результата в БД и возврат его значения"""

    # Запрос значения ID для 'result'
    with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT id_result FROM results
                WHERE result = {result}"""
        )
        id_result = cursor.fetchone()
        if id_result == None:
            return 0
        else:
            return id_result[0]

def select_operation(connection, operand_1, operand_2, operation):

    with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT fk_operation_result FROM operations
                WHERE operand_1 = {operand_1} AND
                operand_2 = {operand_2} AND
                operation = '{operation}'"""
        )
        fk_operation_result = cursor.fetchone()
        if fk_operation_result == None:
            return False
        else:
            return fk_operation_result[0]


def select_result(connection, fk_operation_result):
    """ Поиск результата в БД и возврат его значения"""

    with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT result FROM results
                WHERE id_result = {fk_operation_result}"""
        )
        result = cursor.fetchone()
        if result == None:
            return False
        else:
            return result[0]