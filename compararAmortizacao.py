def simular_financiamento_sac(valor_financiado, juros_anuais, prazo_meses, amortizacao_extra):
    juros_mensais = (1 + juros_anuais) ** (1/12) - 1
    amortizacao_mensal = valor_financiado / prazo_meses

    saldo = valor_financiado
    meses = 0
    total_pago = 0
    juros_total = 0

    while saldo > 0:
        juros_mes = saldo * juros_mensais
        amortizacao = amortizacao_mensal

        # Se o saldo for menor que a amortização + extra, só paga o saldo restante
        if saldo < amortizacao + amortizacao_extra:
            amortizacao_extra = saldo - amortizacao if saldo > amortizacao else 0
            if amortizacao + amortizacao_extra > saldo:
                amortizacao = saldo
                amortizacao_extra = 0

        parcela = amortizacao + juros_mes
        pagamento_total = parcela + amortizacao_extra

        saldo -= (amortizacao + amortizacao_extra)
        if saldo < 0:
            saldo = 0

        total_pago += pagamento_total
        juros_total += juros_mes
        meses += 1

    return meses, total_pago, juros_total

# Parâmetros
valor_financiado = 1_200_000
juros_anuais = 0.085

# Opção 1
prazo1 = 360
parcela_inicial1 = 18_000  # Só para referência (no SAC vai diminuir)
amort_extra1 = 2_000

# Opção 2
prazo2 = 420
parcela_inicial2 = 11_000  # Só para referência
amort_extra2 = 9_000

# Simulações
meses1, total_pago1, juros1 = simular_financiamento_sac(valor_financiado, juros_anuais, prazo1, amort_extra1)
meses2, total_pago2, juros2 = simular_financiamento_sac(valor_financiado, juros_anuais, prazo2, amort_extra2)

print("=== Opção 1 de 18 mil ===")
print(f"Meses para quitar: {meses1}")
print(f"Total pago: R$ {total_pago1:,.2f}")
print(f"Total de juros pagos: R$ {juros1:,.2f}")

print("\n=== Opção 2 de 11 mil ===")
print(f"Meses para quitar: {meses2}")
print(f"Total pago: R$ {total_pago2:,.2f}")
print(f"Total de juros pagos: R$ {juros2:,.2f}")

if total_pago1 < total_pago2:
    print("\nOpção 1 é mais econômica.")
else:
    print("\nOpção 2 é mais econômica.")
