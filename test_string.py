class FraseCom1Vogal():
    frase = 'o sapo nao lava o pe'

    vogais = ['a', 'e', 'i', 'o', 'u']
    frases = []

    def __init__(self):
        for vogal in self.vogais:
            self.frases.append(
                self.getFrases(
                    self.frase,
                    self.vogais.index(vogal)
                )
            )

    def getFrases(self, lin: str, idx: int = 0) -> str:
        vogal = self.vogais[idx]
        for letra in lin:
            if letra in self.vogais and vogal != letra:
                lin = lin.replace(letra, vogal)
        return lin
