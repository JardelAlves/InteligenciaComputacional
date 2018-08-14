class Estado():
    def __init__(self, missionariosEsquerda, missionariosDireita, canibaisEsquerda, canibaisDireita, ladoRio):
        self.missionariosEsquerda = missionariosEsquerda
        self.missionariosDireita = missionariosDireita
        self.canibaisEsquerda = canibaisEsquerda
        self.canibaisDireita = canibaisDireita
        self.ladoRio = ladoRio
        self.pai = None
        self.filhos = []

    def __str__(self):
        return 'Missionarios: {}\t| Missionarios: {}\nCanibais: {}\t| Canibais: {}'.format(self.missionariosEsquerda,
                                                                                           self.missionariosDireita,
                                                                                           self.canibaisEsquerda,
                                                                                           self.canibaisDireita)

    def estadoValido(self):
        if ((self.missionariosEsquerda < 0) or (self.missionariosDireita < 0) or (self.canibaisEsquerda < 0) or (
                self.canibaisDireita < 0)):
            return False
        return ((self.missionariosEsquerda == 0 or self.missionariosEsquerda >= self.canibaisEsquerda) and (
                    self.missionariosDireita == 0 or self.missionariosDireita >= self.canibaisDireita))

    def estadoFinal(self):
        resultadoEsquerda = self.missionariosEsquerda == self.canibaisEsquerda == 0
        resultadoDireita = self.missionariosDireita == self.canibaisDireita == 3
        return resultadoEsquerda and resultadoDireita

    def gerarFilhos(self):
        if self.ladoRio == 'esquerda':
            novoLadoRio = 'direita'
        else:
            novoLadoRio = 'esquerda'

        movimentosBote = [
            {'missionarios': 2, 'canibais': 0},
            {'missionarios': 1, 'canibais': 0},
            {'missionarios': 1, 'canibais': 1},
            {'missionarios': 0, 'canibais': 1},
            {'missionarios': 0, 'canibais': 2},
        ]

        for movimentoAtual in movimentosBote:
            if self.ladoRio == 'esquerda':
                missionariosEsquerda = self.missionariosEsquerda - movimentoAtual['missionarios']
                missionariosDireita = self.missionariosDireita + movimentoAtual['missionarios']
                canibaisEsquerda = self.canibaisEsquerda - movimentoAtual['canibais']
                canibaisDireita = self.canibaisDireita + movimentoAtual['canibais']
            else:
                missionariosDireita = self.missionariosDireita - movimentoAtual['missionarios']
                missionariosEsquerda = self.missionariosEsquerda + movimentoAtual['missionarios']
                canibaisDireita = self.canibaisDireita - movimentoAtual['canibais']
                canibaisEsquerda = self.canibaisEsquerda + movimentoAtual['canibais']
            filho = Estado(missionariosEsquerda, missionariosDireita, canibaisEsquerda, canibaisDireita, novoLadoRio)
            filho.pai = self
            if filho.estadoValido():
                self.filhos.append(filho)


class missionariosCanibais():
    def __init__(self):
        self.filaExecucao = [Estado(3, 0, 3, 0, 'esquerda')]
        self.solucao = None

    def gerarSolucao(self):
        for elemento in self.filaExecucao:
            if elemento.estadoFinal():
                self.solucao = [elemento]
                while elemento.pai:
                    self.solucao.insert(0, elemento.pai)
                    elemento = elemento.pai
                break
            elemento.gerarFilhos()
            self.filaExecucao.extend(elemento.filhos)


def main():
    problema = missionariosCanibais()
    problema.gerarSolucao()
    for estado in problema.solucao:
        print(estado)
        print(34 * '-')


if __name__ == '__main__':
    main()