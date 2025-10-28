def monitorar_temperatura():
    """
    Recebe a temperatura atual e fornece um status de monitoramento
    (Normal, Aviso, Alerta).
    """
    
    # 1. Solicita a temperatura ao usuário e trata possíveis erros de entrada
    while True:
        try:
            # Pede a temperatura e converte para float (para permitir valores decimais)
            temperatura = float(input("Digite a temperatura atual da máquina (°C): "))
            # Garante que a temperatura é um valor razoável (não negativo, por exemplo)
            if temperatura < -273.15: # Ponto mais baixo é o zero absoluto
                 print("Temperatura inválida. Por favor, digite um valor razoável.")
                 continue
            break # Sai do loop se a entrada for válida
        except ValueError:
            # Captura o erro se o usuário digitar algo que não é um número
            print("Entrada inválida. Por favor, digite um número (ex: 75.5).")

    # 2. Lógica de monitoramento
    
    # Alerta (crítico) - se passar de 80°C
    if temperatura > 80:
        print(f"\n🚨 ALERTA CRÍTICO! 🚨")
        print(f"Temperatura atual: {temperatura}°C")
        print("A temperatura passou de 80°C. **ACIONE O SISTEMA DE REFRIGERAÇÃO IMEDIATAMENTE!**")
        
    # Aviso (elevado) - se estiver entre 60°C e 80°C (inclusive 60)
    elif 60 <= temperatura <= 80:
        print(f"\n⚠️ AVISO: TEMPERATURA ELEVADA ⚠️")
        print(f"Temperatura atual: {temperatura}°C")
        print("A temperatura está entre 60°C e 80°C. **MONITORAR DE PERTO.**")
        
    # Normal - se estiver abaixo de 60°C
    else: # temperatura < 60
        print(f"\n✅ STATUS: NORMAL ✅")
        print(f"Temperatura atual: {temperatura}°C")
        print("A temperatura está abaixo de 60°C. Tudo em ordem.")

# Chama a função principal para executar o programa
if __name__ == "__main__":
    monitorar_temperatura()