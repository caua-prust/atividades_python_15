# EXERCÍCIO 8: ALERTA DE MANUTENÇÃO

def alerta_manutencao():
    HORAS_MANUTENCAO = 500
    horas_operacao = 0
    
    print("--- SIMULAÇÃO DE OPERAÇÃO DA MÁQUINA (Loop WHILE) ---")
    print(f"Alerta de Manutenção Programado para: {HORAS_MANUTENCAO} horas")
    print("-" * 60)
    
    while horas_operacao < HORAS_MANUTENCAO:
        
        incremento = 100
        
        if horas_operacao + incremento > HORAS_MANUTENCAO:
            incremento = HORAS_MANUTENCAO - horas_operacao
        
        horas_operacao += incremento
        
        print(f"  Operação em curso: {horas_operacao} horas atingidas.")

    print("\n" + "!"*60)
    print("ALERTA DE MANUTENÇÃO PREVENTIVA!")
    print(f"A máquina atingiu o limite de {horas_operacao} horas.")
    print("Parada Imediata para Manutenção.")
    print("!"*60)
    print("Simulação Encerrada.")

if __name__ == "__main__":
    alerta_manutencao()