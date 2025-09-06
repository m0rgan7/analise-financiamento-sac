valor_inicial = 3491.23
descontos = 416.99 + 6.6
valor_atual = valor_inicial - descontos

rendimento_diario = 1.32

rendimento_mensal = rendimento_diario * 30  # assumindo 30 dias no mês
percentual_mensal = (rendimento_mensal / valor_atual) * 100

print(f"Valor atual: R${valor_atual:.2f}")
print(f"Rendimento mensal aproximado: R${rendimento_mensal:.2f}")
print(f"Percentual mensal aproximado sobre o valor atual: {percentual_mensal:.2f}%")
