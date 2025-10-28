
def identificar_turno():
    """
    Recebe a hora atual (0 a 23) e identifica o turno de operação (Manhã, Tarde, Noite).
    
    Regras:
    - Manhã: 6h às 12h (6, 7, 8, 9, 10, 11)
    - Tarde: 12h às 18h (12, 13, 14, 15, 16, 17)
    - Noite: 18h às 6h (18, 19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5)
    """
    
    print("--- ⏱️ IDENTIFICADOR DE TURNOS ---")
    
    # 1. Solicita a hora atual e garante que é um número inteiro válido (0 a 23)
    while True:
        try:
            # Pede a hora e converte para int
            hora_atual = int(input("Digite a hora atual (formato 24h, ex: 9, 14, 21): "))
            
            # Valida o intervalo de 0 a 23
            if 0 <= hora_atual <= 23:
                 break # Sai do loop se a hora for válida
            else:
                 print("Hora inválida. Por favor, digite um número inteiro entre 0 e 23.")
                 continue
            
        except ValueError:
            # Captura o erro se o usuário digitar algo que não é um número inteiro
            print("Entrada inválida. Por favor, digite apenas a hora como um número inteiro.")

    # 2. Lógica de identificação do turno
    
    # Manhã: 6h (inclusivo) até 12h (exclusivo)
    if 6 <= hora_atual < 12:
        turno = "Manhã ☀️"
        faixa = "6h00 às 11h59"
        
    # Tarde: 12h (inclusivo) até 18h (exclusivo)
    elif 12 <= hora_atual < 18:
        turno = "Tarde 🌤️"
        faixa = "12h00 às 17h59"
        
    # Noite: 18h (inclusivo) até 6h (exclusivo)
    # Esta condição cobre o horário das 18h até 23h, E de 0h até 5h.
    else: # O 'else' pega todos os horários restantes (0, 1, 2, 3, 4, 5 e 18, 19, 20, 21, 22, 23)
        turno = "Noite 🌙"
        faixa = "18h00 às 05h59"
        
    # 3. Exibe o resultado
    print("\n--- ✅ RESULTADO DO CONTROLE DE OPERAÇÃO ---")
    print(f"Hora Informada: **{hora_atual}:00**")
    print(f"Turno Atual: **{turno}**")
    print(f"Faixa de Operação: {faixa}")


# Chama a função principal para executar o programa
if __name__ == "__main__":
    identificar_turno()