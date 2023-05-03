from rentabilidade_prefixado import calcular_rentabilidade_prefixado
from rentabilidade_ipca import calcular_rentabilidade_ipca
from rentabilidade_poupanca import calcular_rentabilidade_poupanca
from rentabilidade_selic import calcular_rentabilidade_selic
from melhor_investimento import calcula_melhor_investimento


if __name__ == "__main__":
    valor_investido = float(input("Digite o valor que será investido: R$"))
    data_inicial = input("Informe a data inicial: (exemplo: 01-02-2003) ")
    data_final = input("Informe a data final: (exemplo: 01-02-2003) ")
    taxa_prefixado = float(input("Digite o valor da taxa prefixada: "))
    spread_selic = float(input("inforne a taxa do spread selic: "))
    taxa_selic = float(input('Informe a taxa selic: '))
    taxa_ipca = float(input("informe o valor da taxa IPCA: "))
    spread_ipca = float(input("informe o valor do spread IPCA: "))
    taxa_poupanca = float(input("informe a taxa da poupança: "))

    # Exemplo para teste:
    # valor_investido = 30000
    # data_inicial = '01-01-2023'
    # data_final = '01-01-2026'
    # taxa_prefixado = 11.83
    # spread_selic = 0.1217
    # taxa_selic = 13.75
    # taxa_ipca = 0.57
    # spread_ipca = 5.7
    # taxa_poupanca = 6.7

    prefixado = calcular_rentabilidade_prefixado(
        valor_investido,
        taxa_prefixado,
        data_inicial,
        data_final
    )
    selic = calcular_rentabilidade_selic(
        valor_investido,
        spread_selic,
        data_inicial,
        data_final,
        taxa_selic
    )
    ipca = calcular_rentabilidade_ipca(
        valor_investido,
        taxa_ipca,
        spread_ipca,
        data_inicial,
        data_final
    )
    poupanca = calcular_rentabilidade_poupanca(
        valor_investido,
        taxa_poupanca,
        data_inicial,
        data_final
    )

    data_dict = {
        'Prefixado': prefixado['rendimento_liquido'] - valor_investido,
        'Selic': selic['rendimento_liquido'] - valor_investido,
        'IPCA': ipca['rendimento_liquido'] - valor_investido,
        'Poupança': poupanca['rendimento_liquido'] - valor_investido,
    }

    melhor_invest = calcula_melhor_investimento(data_dict)

    print(
        f"""Simulação Tesouro Prefixado
                Investimento inicial: R${valor_investido:,.2f}
                Rendimento Líquido no período: R${round(prefixado['rendimento_liquido'], 2) - valor_investido}
                Total Líquido: R$ {round(prefixado['rendimento_liquido'], 2)}
                Taxas Contratadas: {taxa_prefixado:,.2f}%
                Valor Imposto: R${round(prefixado['imposto'], 2) if isinstance(prefixado['imposto'], float) else prefixado['imposto']}

            Simulação Tesouro Selic
                Investimento inicial: R${valor_investido:,.2f}
                Rendimento Líquido no período: R${round(selic['rendimento_liquido'], 2) - valor_investido}
                Total Líquido: R$ {round(selic['rendimento_liquido'], 2)}
                Taxas Contratadas: {(taxa_selic + spread_selic):,.2f}%
                Valor Imposto: R${round(selic['imposto'], 2) if isinstance(selic['imposto'], float) else selic['imposto']}

            Simulação Tesouro IPCA
                Investimento inicial: R${valor_investido:,.2f}
                Rendimento Líquido no período: R${round(ipca['rendimento_liquido'], 2) - valor_investido}
                Total Líquido: R$ {round(ipca['rendimento_liquido'], 2)}
                Taxas Contratadas: {(taxa_ipca + spread_ipca):,.2f}%
                Valor Imposto: R${round(ipca['imposto'], 2) if isinstance(ipca['imposto'], float) else ipca['imposto']}

            Simulação Tesouro Poupança
                Investimento inicial: R${valor_investido:,.2f}
                Rendimento Líquido no período: R${round(poupanca['rendimento_liquido'], 2) - valor_investido}
                Total Líquido: R$ {round(poupanca['rendimento_liquido'], 2)}
                Taxas Contratadas: {taxa_poupanca:,.2f}%
                Valor Imposto: R${round(poupanca['imposto'], 2) if isinstance(poupanca['imposto'], float) else poupanca['imposto']}

            ******* MELHOR INVESTIMENTO ********
                {melhor_invest[0]} rendendo no final do período: R$ {melhor_invest[1]:,.2f}
        """
    )
