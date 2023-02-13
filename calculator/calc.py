"""Калькулятор"""
""" 1. принимает ввод данных от пользователя
       с выводом подсказки вариаций арифметических действий
    2. при вводе букв или неиспользуемых знаков выводит сообщение
       о невозможности использования данных символов
       и предлагает повторить ввод
    3. определяет очерёдность арифметических дейтсвий
    4. производит вычисление в соответствии с очередностью
    5. выводит результат и предлагает произвести новый ввод"""


import re
from sql_manage import check_res_db, paste_new_oper_res, check_operation_db

class Calculator():
    """ содержит методы для обработки вводных данных
        и производства вычислений"""

    def __init__(self):
        # Флаг обработки ввода
        self.active = True
        # Флаг работы программы
        self.run = True

    def add(self, *args):
        """сложение"""
        a = sum(args)
        return self._form(Calculator, a)

    def substract(self, a, b):
        """вычитание"""
        s = a - b
        return self._form(Calculator, s)

    def divide(self, a, b):
        """деление"""
        d = a / b
        return self._form(Calculator, d)

    def multiply(self, a, b):
        """умножение"""
        m = a * b
        return self._form(Calculator, m)

    def _form(self, i):
        """форматирование"""
        i = round(i, 3)
        i_str = str(i)
        if re.match("0.", ''.join(reversed(i_str))):
            return int(i)
        return i

    def _check_symbols(self, string):
        """Проверка вводных данных"""
        # проверка соответствия символов
        symbols = "0123456789/*-+. "
        for char in string:
            if char not in symbols:
                return False
        symb_lst = self._symdol_list(Calculator, string)
        # проверка правильного написания чисел
        for num in symb_lst:
            num = num.replace('.', '')
            if not num.isdigit():
                return False
        # проверка количества чисел
        if len(symb_lst) != 2:
            return False
        return True

    def _symdol_list(self, string):
        """Составление списка из вводных чисел"""
        lst = re.split(r'[/*+-]', string)
        lst = [x.strip() for x in lst]
        return lst

    def calc(self, s):
        """Основной цикл калькуляций"""
        symb_lst = self._symdol_list(Calculator, s)
        a, b = float(symb_lst[0]), float(symb_lst[1])
        if '+' in s:
            res = self.add(Calculator, a, b)
            operator = 'ADD'
        elif '-' in s:
            res = self.substract(Calculator, a, b)
            operator = 'SUBSTR'
        elif '*' in s:
            res = self.multiply(Calculator, a, b)
            operator = 'MLTPL'
        elif '/' in s:
            res = self.divide(Calculator, a, b)
            operator = 'DIV'
        print(f"\nОтвет: {res}\n")


        id_result = check_res_db(result=res)
        if id_result != 0:
            paste_new_oper_res(
                operand_1=a,
                operator=operator,
                operand_2=b,
                id_result=id_result
            )
        else:
            paste_new_oper_res(
                result=res,
                operand_1=a,
                operator=operator,
                operand_2=b
            )

        return res

    def check_db(self, s):
        symb_lst = self._symdol_list(Calculator, s)
        a, b = float(symb_lst[0]), float(symb_lst[1])
        if '+' in s:
            operator = 'ADD'
            res = check_operation_db(operand_1=a, operand_2=b, operation=operator)
        elif '-' in s:
            operator = 'SUBSTR'
            res = check_operation_db(operand_1=a, operand_2=b, operation=operator)
        elif '*' in s:
            operator = 'MLTPL'
            res = check_operation_db(operand_1=a, operand_2=b, operation=operator)
        elif '/' in s:
            operator = 'DIV'
            res = check_operation_db(operand_1=a, operand_2=b, operation=operator)

        if res:
            return res
        else:
            return False

