from calcular_dias import calcula_dias
from imposto_de_renda import calcular_imposto_de_renda


def calcular_rentabilidade_selic(
    valor_investido: float,
    spread_selic: float,
    data_inicial: str,
    data_final: str,
    taxa_selic: float
) -> str:
    tempo = calcula_dias(data_inicial, data_final)
    taxa_selic_total = taxa_selic + spread_selic
    rendimento_selic = valor_investido*(
        1+((taxa_selic_total / 365) / 100))**tempo
    rendimento_bruto = rendimento_selic - valor_investido
    imposto_de_renda = calcular_imposto_de_renda(rendimento_bruto, tempo)
    return {
        "rendimento_liquido": rendimento_selic - imposto_de_renda,
        "imposto": "Isento" if imposto_de_renda == 0 else imposto_de_renda
    }
