# EXERCÍCIO 7: CÁLCULO DE EFICIÊNCIA

def calcular_eficiencia():
    """
    Solicita produção real e esperada, calcula a eficiência
    e classifica a performance da máquina usando IF-ELIF-ELSE.
    """
    print("--- ⚙️ CÁLCULO DE EFICIÊNCIA DA MÁQUINA ⚙️ ---")

    # 1. Receber a Produção Real (com validação para garantir um número positivo)
    while True:
        try:
            # Converte a entrada para float para permitir números decimais
            producao_real = float(input("✅ Digite a **Produção Real** (unidades produzidas): "))
            if producao_real >= 0:
                break
            else:
                print("⚠️ A produção real não pode ser negativa.")
        except ValueError:
            print("❌ Entrada inválida. Por favor, digite um número válido.")

    # 2. Receber a Produção Esperada (com validação para garantir um número positivo > 0)
    while True:
        try:
            producao_esperada = float(input("🎯 Digite a **Produção Esperada** (meta de produção): "))
            if producao_esperada > 0:
                break
            else:
                print("⚠️ A produção esperada deve ser maior que zero para o cálculo.")
        except ValueError:
            print("❌ Entrada inválida. Por favor, digite um número válido.")

    # 3. Calcular a Eficiência
    # Fórmula: (real / esperada) * 100
    eficiencia = (producao_real / producao_esperada) * 100

    # Arredonda a eficiência para duas casas decimais para melhor exibição
    eficiencia_formatada = round(eficiencia, 2)

    # 4. Classificar a Eficiência usando IF/ELIF/ELSE
    mensagem_classificacao = ""
    status_emoji = ""

    if eficiencia_formatada >= 90:
        mensagem_classificacao = "**Excelente**"
        status_emoji = "⭐️"
    elif eficiencia_formatada >= 70:  # Cobre de 70.00% até 89.99%
        mensagem_classificacao = "**Boa**"
        status_emoji = "👍"
    else:  # Cobre tudo abaixo de 70.00%
        mensagem_classificacao = "**Precisa melhorar**"
        status_emoji = "🚨"

    # 5. Mostrar o Resultado
    print("\n" + "="*50)
    print("📊 **RELATÓRIO DE PERFORMANCE**")
    print("-" * 50)
    print(f"   📈 Eficiência Calculada: **{eficiencia_formatada}%**")
    print(f"   {status_emoji} Classificação: {mensagem_classificacao}")
    print("="*50)

# Chama a função principal para executar o programa
if __name__ == "__main__":
    calcular_eficiencia()

        