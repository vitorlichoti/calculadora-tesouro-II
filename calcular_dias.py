from datetime import datetime


def calcula_dias(data_inicial, data_final):
    init_format = datetime.strptime(data_inicial, '%d-%m-%Y')
    final_format = datetime.strptime(data_final, '%d-%m-%Y')
    dias = abs((final_format - init_format).days)
    return dias
