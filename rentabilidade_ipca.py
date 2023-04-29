from calcular_dias import calcula_dias
from imposto_de_renda import calcular_imposto_de_renda


def calcular_rentabilidade_ipca(
    valor_investido: float,
    taxa_ipca: float,
    spread_ipca: float,
    data_inicial: str,
    data_final: str,
) -> str:
    tempo = calcula_dias(data_inicial, data_final)
    taxa_ipca_total = (taxa_ipca + spread_ipca)
    rendimento_ipca = valor_investido*(
        1+((taxa_ipca_total / 365) / 100))**tempo
    rendimento_bruto = rendimento_ipca - valor_investido
    imposto_de_renda = calcular_imposto_de_renda(rendimento_bruto, tempo)
    return {
        "rendimento_liquido": rendimento_ipca - imposto_de_renda,
        "imposto": "Isento" if imposto_de_renda == 0 else imposto_de_renda
    }
