"""taxas de impost de renda baseado no site:
https://artigos.toroinvestimentos.com.br/irpf/tabela-do-imposto-de-renda"""


def calcular_imposto_de_renda(rendimento: float, prazo: float) -> str:
    anual = prazo // 365
    if rendimento >= 1903.99 and rendimento <= 2826.65:
        return rendimento * 0.075 * anual
    if rendimento >= 2826.66 and rendimento <= 3751.05:
        return rendimento * 0.15 * anual
    if rendimento >= 3751.06 and rendimento <= 4664.68:
        return rendimento * 0.15 * anual
    if rendimento >= 4664.68:
        return rendimento * 0.275 * anual
    return 0
