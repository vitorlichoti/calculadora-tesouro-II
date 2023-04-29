def calcula_melhor_investimento(
    data: dict
):
    values = [data[item] for item in data]
    value_max = max(values)
    name = [item for item in data if data[item] == value_max]
    return (name[0], value_max)
