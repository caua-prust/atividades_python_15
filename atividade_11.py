
def controle_qualidade_lote():
    
    DEFEITOS_MAX_SEGUIDOS = 5
    
    pecas_boas = 0
    defeitos_seguidos = 0
    total_pecas_inspecionadas = 0
    
    print("--- CONTROLE DE QUALIDADE POR LOTE ---")
    print(f"Parada de inspeção após {DEFEITOS_MAX_SEGUIDOS} defeitos seguidos.")
    print("-" * 50)
    
    
    while defeitos_seguidos < DEFEITOS_MAX_SEGUIDOS:
        
        total_pecas_inspecionadas += 1
        
       
        while True:
            status_peca = input(f"Peça {total_pecas_inspecionadas}. Digite 'B' (Boa) ou 'D' (Defeituosa): ").upper()
            if status_peca in ('B', 'D'):
                break
            else:
                print("Entrada inválida. Digite apenas 'B' ou 'D'.")
        
       
        if status_peca == 'B':
            pecas_boas += 1
            defeitos_seguidos = 0  
            print("Status: Peça Boa. Reiniciando contagem de defeitos seguidos.")
        
        elif status_peca == 'D':
            defeitos_seguidos += 1
            print(f"Status: Peça Defeituosa. Defeitos seguidos: {defeitos_seguidos}")
            
        print("-" * 50) 
   
    print("\n" + "#"*50)
    print("!!! INSPEÇÃO PARADA !!!")
    print(f"Motivo: {DEFEITOS_MAX_SEGUIDOS} defeitos consecutivos encontrados.")
    print(f"Total de peças inspecionadas: {total_pecas_inspecionadas}")
    print(f"TOTAL DE PEÇAS BOAS NO LOTE: {pecas_boas}")
    print("#"*50)


if __name__ == "__main__":
    controle_qualidade_lote()