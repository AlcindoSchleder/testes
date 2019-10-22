frase = 'o sapo nao lava o pe'

vogais = ['a', 'e', 'i', 'o', 'u']
frases = []

def getFrases(lin: str, idx: int = 0) -> str:
    vogal = vogais[idx]
    for letra in lin:
        if ((letra in vogais) and (vogal != letra)):
            lin = lin.replace(letra, vogal)
    return lin

for vogal in vogais:
    frases.append(getFrases(frase, vogais.index(vogal)))
  
print(frases)
