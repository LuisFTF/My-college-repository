# Função que retorna True se o número for primo
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Testa de 1 a 100
for num in range(1, 101):
    if eh_primo(num):
        print(num, "é primo")
