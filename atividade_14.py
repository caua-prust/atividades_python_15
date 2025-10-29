def classificar_produto():
    """
    Recebe dados de peso e status de defeito e classifica o produto final.
    """
    
    PESO_IDEAL_MIN = 98.0
    PESO_IDEAL_MAX = 102.0
    PESO_PADRAO_MIN = 95.0
    PESO_PADRAO_MAX = 105.0
    
    print("--- CLASSIFICAÇÃO DE PRODUTOS FINAIS ---")
    
    # 1. Receber o peso do produto
    while True:
        try:
            peso = float(input("Digite o peso do produto (em gramas): "))
            if peso > 0:
                break
            else:
                print("O peso deve ser um valor positivo.")
        except ValueError:
            print("Entrada inválida. Digite um número para o peso.")

    # 2. Receber status de defeito
    while True:
        tem_defeito = input("O produto tem defeitos? (S/N): ").upper()
        if tem_defeito in ('S', 'N'):
            break
        else:
            print("Entrada inválida. Digite apenas S (Sim) ou N (Não).")
            
    # 3. Classificação do Produto
    
    classificacao = ""
    
    # Condição 1: PREMIUM
    # Peso IDEAL (98-102) E Sem Defeitos
    if PESO_IDEAL_MIN <= peso <= PESO_IDEAL_MAX and tem_defeito == 'N':
        classificacao = "Premium (Peso Ideal e Sem Defeitos)"
        
    # Condição 2: STANDARD
    # Está dentro do PADRÃO MÍNIMO (95-105) E não é Premium
    # OU Está no peso ideal mas tem algum defeito
    elif PESO_PADRAO_MIN <= peso <= PESO_PADRAO_MAX:
        if tem_defeito == 'S':
            classificacao = "Standard (Pequenas Variações - Tem Defeito Leve)"
        else:
            # Não é Premium por não estar no peso IDEAL, mas está no peso padrão
            classificacao = "Standard (Pequenas Variações - Peso)"
            
    # Condição 3: REJEITADO
    # Se não atendeu nenhuma das condições acima (fora do peso padrão MÍNIMO/MÁXIMO)
    else:
        classificacao = "Rejeitado (Fora dos Padrões de Peso ou Defeito Grave)"
        
    # 4. Mostrar o Resultado
    print("-" * 50)
    print(f"Produto Classificado como: **{classificacao}**")
    print("-" * 50)

# Chama a função principal
if __name__ == "__main__":
    classificar_produto()