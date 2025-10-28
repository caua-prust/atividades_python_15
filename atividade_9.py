# EXERCÍCIO 9: CÁLCULO DE CONSUMO ENERGÉTICO

def calcular_consumo_fabrica():
    
    NUMERO_DE_MAQUINAS = 5
    consumo_total = 0.0
    
    print("--- CÁLCULO DE CONSUMO ENERGÉTICO DA FÁBRICA ---")
    print(f"Analisando o consumo de {NUMERO_DE_MAQUINAS} máquinas.")
    print("-" * 50)
    
    for i in range(1, NUMERO_DE_MAQUINAS + 1):
        while True:
            try:
                consumo_maquina = float(input(f"Digite o consumo da Máquina {i} (kWh): "))
                if consumo_maquina >= 0:
                    break
                else:
                    print("O consumo não pode ser negativo.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
        
        consumo_total += consumo_maquina
        
    print("\n" + "="*50)
    print("RELATÓRIO DE CONSUMO ENERGÉTICO")
    print(f"Total de Máquinas Analisadas: {NUMERO_DE_MAQUINAS}")
    print(f"CONSUMO TOTAL DA FÁBRICA: {consumo_total:.2f} kWh")
    print("="*50)

if __name__ == "__main__":
    calcular_consumo_fabrica()