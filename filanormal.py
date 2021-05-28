class FilaNormal:
    codigo: int = 0
    fila = []
    clientesatendidos = []
    senhaatuaql: str = ""

    def gerarsenhaatual(self) -> None:
        self.senhaatuaql = f'NM{self.codigo}'

    def resetafila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualizafila(self) -> None:
        self.resetafila()
        self.gerarsenhaatual()
        self.fila.append(self.senhaatuaql)

    def chamaclient(self, caixa: int) -> str:
        client_atual: str = self.fila.pop(0)
        self.clientesatendidos.append(client_atual)

        return (f'Cliente atual: {client_atual}, dirija-se ao caixa: {caixa}')
