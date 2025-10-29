
def controlar_velocidade():
    """
    Recebe o tipo de produto (A, B ou C) e ajusta a velocidade da esteira.
    """
    
    print("--- CONTROLE DE VELOCIDADE DA ESTEIRA ---")
    
   
    while True:
        tipo_produto = input("Digite o tipo de produto (A, B ou C): ").upper()
        if tipo_produto in ('A', 'B', 'C'):
            break
        else:
            print("Tipo de produto inválido. Digite apenas A, B ou C.")

    velocidade_ajustada = 0
    
    
    if tipo_produto == 'A':
        velocidade_ajustada = 1
        print(f"Produto tipo {tipo_produto} selecionado.")
        
    elif tipo_produto == 'B':
        velocidade_ajustada = 2
        print(f"Produto tipo {tipo_produto} selecionado.")
        
    elif tipo_produto == 'C':
        velocidade_ajustada = 3
        print(f"Produto tipo {tipo_produto} selecionado.")
        
    
    print("-" * 40)
    print(f"⚙️ Velocidade Ajustada: **{velocidade_ajustada}**")
    print("Ajuste concluído.")
    print("-" * 40)


if __name__ == "__main__":
    controlar_velocidade()