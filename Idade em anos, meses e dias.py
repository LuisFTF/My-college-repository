# Programa que lê a idade em dias e converte para anos, meses e dias
dias_totais = int(input("Digite a idade em dias: "))

anos = dias_totais // 365
meses = (dias_totais % 365) // 30
dias = (dias_totais % 365) % 30

print(f"{anos} ano(s), {meses} mês(es) e {dias} dia(s)")
