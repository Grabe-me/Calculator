from django.shortcuts import render, redirect

from createdb import CreateDB
from .forms import OperationForm
from .calc import Calculator
from sql_manage import get_table_data_db

def operation(request):
    create_db = CreateDB()
    create_db.results_table()
    create_db.operations_table()
    form = OperationForm(request.POST or None)
    if form.is_valid():
        form.save()
        oper = form.get_operation()
        calc = Calculator
        grrr = calc._check_symbols(Calculator, oper)
        print(grrr)
        if calc._check_symbols(Calculator, oper):
            if calc.check_db(Calculator, oper):
                rslt = calc.check_db(Calculator, oper)
            else:
                rslt = calc.calc(Calculator, oper)
            return render(request, 'result.html', {'rslt': rslt})
        else:
            input_error = 'Неверный ввод. Допустимые символы: 0123456789/*-+.'
            context = {'form': form, 'input_error': input_error}
            return render(request, 'operation.html', context)
    context = {'form': form, 'input_error': ''}
    return render(request, 'operation.html', context)

def result(request, rslt):
    context = {'rslt': rslt[0]}
    return render(request, 'result.html', context)


def table(request):
    data_table = get_table_data_db()
    context = {'data_table': data_table}
    return render(request, 'table.html', context)

# Create your views here.
