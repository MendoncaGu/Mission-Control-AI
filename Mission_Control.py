
NOME_MISSAO = "60 Parsecs"
NOME_EQUIPE = "Bravo Six"

dados_missao = [
    [23, 93, 85, 97, 91],
    [26, 84, 71, 96, 86],
    [32, 68, 56, 92, 74],
    [38, 44, 35, 86, 52],
    [42, 31, 21, 75, 38],
    [37, 52, 30, 80, 54],
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional",
]

def analisar_temperatura(valor):

    if valor < 18:
        return "ATENÇÃO", 1, "Temperatura muito baixa"
    elif valor <= 30:
        return "NORMAL", 0, "Temperatura estável"
    elif valor <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"
    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"


def analisar_comunicacao(valor):

    if valor < 30:
        return "CRÍTICO", 2, "Sem comunicação"
    elif valor < 60:
        return "ATENÇÃO", 1, "Comunicação instável"
    else:
        return "NORMAL", 0, "Comunicação estável"


def analisar_bateria(valor):

    if valor < 20:
        return "CRÍTICO", 2, "Bateria em nível crítico"
    elif valor < 50:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estável"


def analisar_oxigenio(valor):

    if valor < 80:
        return "CRÍTICO", 2, "Oxigênio em nível crítico"
    elif valor < 90:
        return "ATENÇÃO", 1, "Oxigênio baixo"
    else:
        return "NORMAL", 0, "Oxigênio adequado"


def analisar_estabilidade(valor):

    if valor < 40:
        return "CRÍTICO", 2, "Estabilidade operacional em níveis críticos"
    elif valor < 70:
        return "ATENÇÃO", 1, "Estabilidade operacional reduzida"
    else:
        return "NORMAL", 0, "Estabilidade operacional adequada"


def classificar_ciclo(pontuacao):

    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def gerar_recomendacao(classificacao_ciclo, resultados_ciclo):

    if classificacao_ciclo == "MISSÃO ESTÁVEL":
        return "Manter operação normal e continuar monitoramento."

    recomendacoes = []

    for nome_area, classificacao, _, _ in resultados_ciclo:
        if classificacao == "CRÍTICO":

            if nome_area == "Temperatura interna":
                recomendacoes.append("verificar controle térmico da missão imediatamente!")
            elif nome_area == "Comunicação com a base":
                recomendacoes.append("tentar restabelecer contato com a base com urgência!")
            elif nome_area == "Sistema de energia":
                recomendacoes.append("Recomenda-se ativar modo de economia de energia")
            elif nome_area == "Suporte de oxigênio":
                recomendacoes.append("acionar protocolo de suporte à vida agora!")
            elif nome_area == "Estabilidade operacional":
                recomendacoes.append("Recomenda-se reduzir operações não essenciais")



    if len(recomendacoes) >= 3:
        return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação!"


    if recomendacoes:
        return "Ações urgentes: " + "; ".join(recomendacoes) + "."


    return "Monitorar sistemas em atenção e preparar plano de ação."


def analisar_tendencia(riscos_por_ciclo):

    risco_inicial = riscos_por_ciclo[0]
    risco_final = riscos_por_ciclo[-1]

    if risco_final > risco_inicial:
        return "A missão apresentou tendência de piora."
    elif risco_final < risco_inicial:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."


def identificar_area_mais_afetada(pontuacao_acumulada_por_area):

    area_mais_afetada = None
    maior_pontuacao = -1


    for area, pontuacao in pontuacao_acumulada_por_area.items():
        if pontuacao > maior_pontuacao:
            maior_pontuacao = pontuacao
            area_mais_afetada = area

    return area_mais_afetada


def gerar_relatorio_final(
    riscos_por_ciclo,
    ciclo_mais_critico,
    pontuacao_acumulada_por_area,
    medias
):

    separador = "=" * 60
    print(f"\n{separador}")
    print("RELATÓRIO FINAL DA MISSÃO")
    print(separador)

    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")


    print(f"\nMédia de temperatura:   {medias[0]:.2f} °C")
    print(f"Média de comunicação:   {medias[1]:.2f}%")
    print(f"Média de bateria:       {medias[2]:.2f}%")
    print(f"Média de oxigênio:      {medias[3]:.2f}%")
    print(f"Média de estabilidade:  {medias[4]:.2f}%")


    maior_risco = max(riscos_por_ciclo)
    risco_medio = sum(riscos_por_ciclo) / len(riscos_por_ciclo)
    qtd_criticos = sum(1 for r in riscos_por_ciclo if r >= 6)

    print(f"\nCiclo mais crítico:         Ciclo {ciclo_mais_critico + 1}")
    print(f"Maior pontuação de risco:   {maior_risco}")
    print(f"Risco médio da missão:      {risco_medio:.2f}")
    print(f"Quantidade de ciclos críticos: {qtd_criticos}")


    tendencia = analisar_tendencia(riscos_por_ciclo)
    print(f"\nTendência da missão:")
    print(f"  {tendencia}")


    print("\nPontuação acumulada por área:")
    for area, pontos in pontuacao_acumulada_por_area.items():
        print(f"  {area}: {pontos} ponto(s)")


    area_mais_afetada = identificar_area_mais_afetada(pontuacao_acumulada_por_area)
    print(f"\nÁrea mais afetada:")
    print(f"  {area_mais_afetada}")


    classificacao_final = classificar_ciclo(round(risco_medio))
    print(f"\nClassificação final da missão:")
    print(f"  {classificacao_final}")


    print("\nConclusão:")
    print(
        "A missão demonstrou instabilidade consideravel durante a operação. "
        "Mesmo com a tentativa de recuperação no último ciclo, ainda é possivel observar "
        "sistemas em atenção e a equipe deve continuar mantendo o plano de contingência ativo."
    )
    print(separador)




def main():
    separador_grande = "=" * 60
    separador_pequeno = "-" * 60

    print(separador_grande)
    print("MISSION CONTROL AI")
    print(separador_grande)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print(separador_grande)


    riscos_por_ciclo = []
    ciclo_mais_critico = 0
    maior_risco_registrado = -1


    pontuacao_acumulada_por_area = {area: 0 for area in areas_monitoradas}


    totais_por_coluna = [0, 0, 0, 0, 0]

    for indice_ciclo, ciclo in enumerate(dados_missao):


        temperatura  = ciclo[0]
        comunicacao  = ciclo[1]
        bateria      = ciclo[2]
        oxigenio     = ciclo[3]
        estabilidade = ciclo[4]


        totais_por_coluna[0] += temperatura
        totais_por_coluna[1] += comunicacao
        totais_por_coluna[2] += bateria
        totais_por_coluna[3] += oxigenio
        totais_por_coluna[4] += estabilidade

        print(f"\nCICLO {indice_ciclo + 1}")
        print(separador_pequeno)


        resultado_temp  = ("Temperatura interna",      *analisar_temperatura(temperatura))
        resultado_com   = ("Comunicação com a base",   *analisar_comunicacao(comunicacao))
        resultado_bat   = ("Sistema de energia",       *analisar_bateria(bateria))
        resultado_oxi   = ("Suporte de oxigênio",      *analisar_oxigenio(oxigenio))
        resultado_est   = ("Estabilidade operacional", *analisar_estabilidade(estabilidade))


        resultados_ciclo = [
            resultado_temp,
            resultado_com,
            resultado_bat,
            resultado_oxi,
            resultado_est,
        ]


        unidades = ["°C", "%", "%", "%", "%"]
        valores = [temperatura, comunicacao, bateria, oxigenio, estabilidade]

        pontuacao_ciclo = 0

        for i, (nome_area, classificacao, pontos, mensagem) in enumerate(resultados_ciclo):
            unidade = unidades[i]
            valor = valores[i]
            print(f"  {nome_area}: {valor}{unidade} | {classificacao} | {mensagem}")


            pontuacao_ciclo += pontos


            pontuacao_acumulada_por_area[nome_area] += pontos


        classificacao_ciclo = classificar_ciclo(pontuacao_ciclo)

        print(f"\n  Pontuação de risco do ciclo: {pontuacao_ciclo}")
        print(f"  Classificação do ciclo: {classificacao_ciclo}")


        recomendacao = gerar_recomendacao(classificacao_ciclo, resultados_ciclo)
        print(f"  Recomendação: {recomendacao}")


        riscos_por_ciclo.append(pontuacao_ciclo)


        if pontuacao_ciclo > maior_risco_registrado:
            maior_risco_registrado = pontuacao_ciclo
            ciclo_mais_critico = indice_ciclo


    quantidade_ciclos = len(dados_missao)
    medias = [total / quantidade_ciclos for total in totais_por_coluna]


    gerar_relatorio_final(
        riscos_por_ciclo,
        ciclo_mais_critico,
        pontuacao_acumulada_por_area,
        medias
    )

if __name__ == "__main__":
    main()