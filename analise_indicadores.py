    print("INDICADORES DE QUALIDADE EM NUTRIÇÃO HOSPITALAR")
    print("-" * 50)

    for linha in dados:
        total = int(linha["total_admissoes"])

        triagem = calcular_percentual(
            int(linha["triagem_em_24h"]), total
        )

        avaliacao = calcular_percentual(
            int(linha["avaliacao_nutricional_concluida"]), total
        )

        print(f"\nPeríodo: {linha['mes']}")
        print(f"Triagem em até 24h: {triagem:.1f}%")
        print(f"Avaliação nutricional concluída: {avaliacao:.1f}%")
