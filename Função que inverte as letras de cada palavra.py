# Função que inverte cada palavra de uma frase
def inverte_palavras(frase):
    palavras = frase.split()
    palavras_invertidas = [palavra[::-1] for palavra in palavras]
    return " ".join(palavras_invertidas)

# Exemplo de uso
frase = input("Digite uma frase: ")
nova_frase = inverte_palavras(frase)
print("Frase invertida:", nova_frase)
