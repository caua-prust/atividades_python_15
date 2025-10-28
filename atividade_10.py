

import random

def verificar_sensor():
    """
    Simula a leitura de um sensor, verifica se o valor está dentro da faixa
    normal (1 a 100) e classifica o status do sensor.
    """
    
    
    leitura_sensor = random.randint(-20, 150)
    
    LIMITE_MIN = 1
    LIMITE_MAX = 100
    
    print("--- VERIFICAÇÃO DE SENSOR IoT ---")
    print(f"Valor lido do Sensor: {leitura_sensor}")
    print(f"Faixa esperada: {LIMITE_MIN} a {LIMITE_MAX}")
    print("-" * 35)
    
   
    
    
    if LIMITE_MIN <= leitura_sensor <= LIMITE_MAX:
        status = "Sensor OK"
        print("✅ Status: " + status)
    
    else:
        status = "Sensor com problema"
        print("❌ Status: " + status)
        
    print("-" * 35)
    

if __name__ == "__main__":
    
    print("Teste 1:")
    verificar_sensor()
    print("\nTeste 2:")
    verificar_sensor()
    print("\nTeste 3:")
    verificar_sensor()