def controle_qualidade():
    """
    Recebe o número de defeitos e aprova ou reprova a peça com base na regra:
    Aprovar: até 2 defeitos
    Reprovar: mais de 2 defeitos
    """
    
    LIMITE_DEFEITOS = 2
    
    print("--- ⚙️ INSPEÇÃO DE CONTROLE DE QUALIDADE ---")
    print(f"O limite máximo para aprovação é de {LIMITE_DEFEITOS} defeitos.")
    
    # 1. Solicita o número de defeitos e garante que é um número inteiro não negativo
    while True:
        try:
            # Pede o número de defeitos e converte para int
            num_defeitos = int(input("Digite o número de defeitos encontrados na peça: "))
            
            # Garante que o número de defeitos não é negativo
            if num_defeitos < 0:
                 print("O número de defeitos não pode ser negativo. Tente novamente.")
                 continue
            break # Sai do loop se a entrada for válida
            
        except ValueError:
            # Captura o erro se o usuário digitar algo que não é um número inteiro
            print("Entrada inválida. Por favor, digite um número inteiro (ex: 1, 2 ou 3).")

    # 2. Lógica de classificação
    
    # Reprovar: mais de 2 defeitos (num_defeitos > 2)
    if num_defeitos > LIMITE_DEFEITOS:
        status = "REPROVADA"
        mensagem = f"A peça excedeu o limite de {LIMITE_DEFEITOS} defeitos."
        
    # Aprovar: até 2 defeitos (num_defeitos <= 2)
    else:
        status = "APROVADA"
        
        if num_defeitos == 0:
            mensagem = "Peça de qualidade excelente! Zero defeitos encontrados."
        else: # 1 ou 2 defeitos
            mensagem = f"A peça está dentro do limite e possui {num_defeitos} defeito(s)."
        
    # 3. Exibe o resultado
    print("\n--- ✅ RESULTADO DA INSPEÇÃO ---")
    print(f"Número de Defeitos: **{num_defeitos}**")
    print(f"Status da Peça: **{status}**")
    print(f"Mensagem: {mensagem}")


# Chama a função principal para executar o programa
if __name__ == "__main__":
    controle_qualidade()
