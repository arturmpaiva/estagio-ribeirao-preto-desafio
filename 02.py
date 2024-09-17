texto = input('Digite algo: ')

def contar_letra_a(textoDigitado):
    count = textoDigitado.lower().count('a')

    if count > 0:
        return f"A letra 'a' aparece {count} vezes na string."
    else:
        return "A letra 'a' não foi encontrada na string."

print(contar_letra_a(texto))