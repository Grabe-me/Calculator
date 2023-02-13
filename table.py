from sql_manage import get_max_row

def create_table(data_tup):
    max_row = get_max_row()
    tabel_string = ""
    for i in range(1, max_row):
        tr_open = "<tr>"
        tabel_string += tr_open
        for d in data_tup:
            data = f"<td>{d}</td>"
            tabel_string += data
        tr_close ="</tr>"
        tabel_string += tr_close
    return tabel_string
