

def gerenciar_estoque(estoque_atual):
    """
    Monitora o estoque e alerta sobre a necessidade de reposição.
    """
    
    LIMITE_ALERTA = 50
    SUGESTAO_PEDIDO = 200 
    
    print("--- GERENCIAMENTO DE ESTOQUE ---")
    print(f"Estoque Atual: {estoque_atual} unidades")
    print(f"Limite de Alerta: {LIMITE_ALERTA} unidades")
    print("-" * 40)
    
   
    if estoque_atual < LIMITE_ALERTA:
      
        print("🚨 ALERTA: ESTOQUE BAIXO!")
        print(f"O estoque atual ({estoque_atual}) está abaixo do limite de {LIMITE_ALERTA} unidades.")
        
        
        print(f"✔️ Sugestão de Reposição: Pedir {SUGESTAO_PEDIDO} unidades para reabastecimento.")
        
    else:
        
        print("✅ ESTOQUE OK.")
        print("Nível de estoque seguro.")
    
    print("-" * 40)


print("SIMULAÇÃO 1:")
estoque_simulado_1 = 45
gerenciar_estoque(estoque_simulado_1)


print("\nSIMULAÇÃO 2:")
estoque_simulado_2 = 120
gerenciar_estoque(estoque_simulado_2)


print("\nSIMULAÇÃO 3:")
estoque_simulado_3 = 49
gerenciar_estoque(estoque_simulado_3)