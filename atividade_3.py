

def classificar_peca():
    """
    Recebe o peso de uma peça e a classifica em Leve, Média, Pesada ou Muito Pesada.
    """
    
    print("--- ⚖️ CLASSIFICAÇÃO DE PEÇAS POR PESO ---")
    
    # 1. Solicita o peso da peça e garante que é um número positivo
    while True:
        try:
            # Pede o peso e converte para float (para permitir valores decimais)
            peso_peca = float(input("Digite o peso da peça em quilogramas (kg): "))
            
            # Garante que o peso é positivo
            if peso_peca <= 0:
                 print("O peso deve ser um valor positivo (maior que zero). Tente novamente.")
                 continue
            break # Sai do loop se a entrada for válida
            
        except ValueError:
            # Captura o erro se o usuário digitar algo que não é um número
            print("Entrada inválida. Por favor, digite um número (ex: 1.75 ou 5.2).")

    # 2. Lógica de classificação
    
    # Muito Pesada: acima de 5kg
    if peso_peca > 5.0:
        categoria = "Muito Pesada"
        mensagem = "Utilize um guindaste ou equipamento de movimentação adequado."
        
    # Pesada: 2kg a 5kg
    elif peso_peca > 2.0:  # Isso cobre > 2.0 e <= 5.0 (graças ao 'if' anterior)
        categoria = "Pesada"
        mensagem = "Requer cuidado e possivelmente dois operadores."
        
    # Média: 0,5kg a 2kg
    elif peso_peca > 0.5: # Isso cobre > 0.5 e <= 2.0 (graças aos 'if's anteriores)
        categoria = "Média"
        mensagem = "Pode ser manuseada por uma pessoa com esforço moderado."
        
    # Leve: até 0,5kg (incluindo 0,5kg, já que 0.5 < 0.5 é falso)
    else: # Isso cobre peso_peca <= 0.5 e peso_peca > 0 (garantido pelo while loop)
        categoria = "Leve"
        mensagem = "Fácil de manusear."
        
    # 3. Exibe o resultado
    print("\n--- ✅ RESULTADO DA CLASSIFICAÇÃO ---")
    print(f"Peso da Peça: **{peso_peca} kg**")
    print(f"Classificação: **{categoria}**")
    print(f"Recomendação: {mensagem}")


# Chama a função principal para executar o programa
if __name__ == "__main__":
    classificar_peca()