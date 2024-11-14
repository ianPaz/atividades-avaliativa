def desenhar_retangulo(linhas=1, colunas=1):
    # Garantir que os valores de linhas e colunas estão no intervalo de 1 a 20
    #se não for digitado dentro dos limites, automaticamente vai pra 20/20
    linhas = max(1, min(linhas, 20))
    colunas = max(1, min(colunas, 20))
    
    # Desenhar o retângulo
    for i in range(linhas):
        if i == 0 or i == linhas - 1:  # Primeira ou última linha
            print('+' + '-' * (colunas - 2) + '+')
        else:  # Linhas intermediárias
            print('|' + ' ' * (colunas - 2) + '|')

# Teste da função
linhas = int(input("Digite o número de linhas (1-20): "))
colunas = int(input("Digite o número de colunas (1-20): "))

desenhar_retangulo(linhas, colunas)
