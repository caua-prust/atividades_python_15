# EXERCÍCIO 15: DASHBOARD DE PRODUÇÃO

def dashboard_producao():
    
    NUMERO_LINHAS = 5
    producoes = []
    
    print("--- DASHBOARD DE PRODUÇÃO DA FÁBRICA ---")
    
    # 1. Usar FOR para 5 linhas e registrar a produção
    for i in range(1, NUMERO_LINHAS + 1):
        while True:
            try:
                # Entrada de dados (input())
                producao = int(input(f"Digite a produção da Linha {i} (unidades): "))
                if producao >= 0:
                    producoes.append(producao)
                    break
                else:
                    print("A produção deve ser um número não negativo.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")
    
    # 2. Calcule produção total
    producao_total = sum(producoes)
    
    # 3. Identificar linha com maior produção
    # Encontra o valor máximo na lista
    maior_producao = -1
    linha_maior_producao = -1
    
    # Usa FOR com enumerate para encontrar o índice da maior produção
    for indice, valor in enumerate(producoes):
        # Usa IF para decisões
        if valor > maior_producao:
            maior_producao = valor
            # O índice da lista (começa em 0) corresponde ao número da linha (começa em 1)
            linha_maior_producao = indice + 1
            
    # 4. Mostrar produção de cada linha e resultados (print())
    print("\n" + "="*50)
    print("📊 RELATÓRIO DE PRODUÇÃO GERAL")
    print("-" * 50)
    
    print("PRODUÇÃO POR LINHA:")
    for i in range(NUMERO_LINHAS):
        print(f"  Linha {i + 1}: {producoes[i]} unidades")
        
    print("-" * 50)
    print(f"🏭 PRODUÇÃO TOTAL DA FÁBRICA: {producao_total} unidades")
    print(f"⭐ LINHA COM MAIOR PRODUÇÃO: Linha {linha_maior_producao} ({maior_producao} unidades)")
    print("="*50)

# Chama a função principal
if __name__ == "__main__":
    dashboard_producao()