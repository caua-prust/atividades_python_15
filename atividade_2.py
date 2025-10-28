def controle_producao():
    """
    Recebe a quantidade produzida, compara com a meta de 1000 unidades, 
    e informa o status.
    """
    
    META_DIARIA = 1000
    
    print("--- 🏭 CONTROLE DE PRODUÇÃO DIÁRIA ---")
    print(f"A meta diária é de {META_DIARIA} unidades.")
    
    # 1. Solicita a quantidade produzida e garante que é um número inteiro positivo
    while True:
        try:
            # Pede a quantidade e converte para int
            producao_atual = int(input("Digite a quantidade de unidades produzidas hoje: "))
            
            # Garante que a produção não é negativa
            if producao_atual < 0:
                 print("A produção não pode ser negativa. Por favor, digite um valor válido.")
                 continue
            break # Sai do loop se a entrada for válida
            
        except ValueError:
            # Captura o erro se o usuário digitar algo que não é um número inteiro
            print("Entrada inválida. Por favor, digite um número inteiro (ex: 950).")

    # 2. Lógica de comparação e cálculo
    
    # Verifica se a meta foi atingida
    if producao_atual >= META_DIARIA:
        # Calcula o quanto foi produzido acima da meta
        excedente = producao_atual - META_DIARIA
        
        print("\n🏆 RESULTADO: META ATINGIDA! 🏆")
        print(f"Produção total: **{producao_atual}** unidades.")
        
        # Se houve produção excedente
        if excedente > 0:
            print(f"Parabéns! Você **superou a meta** em **{excedente}** unidades!")
        else: # Produziu exatamente 1000
             print("A meta foi atingida com exatidão!")
             
    # A meta NÃO foi atingida
    else:
        # Calcula quantas unidades faltaram para atingir a meta
        faltante = META_DIARIA - producao_atual
        
        print("\n❌ RESULTADO: META NÃO ATINGIDA ❌")
        print(f"Produção total: **{producao_atual}** unidades.")
        print(f"Faltaram **{faltante}** unidades para alcançar a meta de {META_DIARIA}.")
        
        if faltante > META_DIARIA / 2: 
             print("É necessário revisar o processo de produção para o próximo dia.")
        else:
             print("Foco total para alcançar a meta amanhã!")



if __name__ == "__main__":
    controle_producao()