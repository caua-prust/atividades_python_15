
def contador_producao_turno():
    
    producao_total = 0

    
    horas_do_turno = 8

   
    for hora in range(1, horas_do_turno + 1):
        
        while True:
            try:
                
                producao_horaria = int(input(f"🛠️ Digite a produção da hora {hora} (unidades): "))
                if producao_horaria >= 0:
                    break  
                else:
                    print("⚠️ A produção deve ser um número positivo ou zero.")
            except ValueError:
                print("❌ Entrada inválida. Por favor, digite um número inteiro.")


        producao_total += producao_horaria

   
    print("\n" + "="*40)
    print(f"📊 **RELATÓRIO FINAL DE PRODUÇÃO DO TURNO**")
    print(f"🕰️ Total de Horas no Turno: {horas_do_turno}")
    print(f"🏭 **PRODUÇÃO TOTAL DO TURNO: {producao_total} unidades**")
    print("="*40)


if __name__ == "__main__":
    contador_producao_turno()