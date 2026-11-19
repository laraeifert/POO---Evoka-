class Treinos:

    ESTABELECIMENTOS = [
        {"nome": "Padaria Pão Quente", "endereco": "Av. Guilherme Schell, 100", "bairro": "Centro"},
        {"nome": "Academia Corpo em Forma", "endereco": "Av. Guilherme Schell, 250", "bairro": "Centro"},
        {"nome": "Farmácia Saúde", "endereco": "Rua Tiradentes, 45", "bairro": "Centro"},
    ]
    km_final = None
    tempo_exec = None
    pessoa = None
    __estabelecimento = None 


    def __init__(self, localizacao: str, km_inicial: float, nome: str):
        self.nome = nome
        self.localizacao = localizacao
        self.km_inicial = km_inicial

    def procura_estabelecimento(self, endereco: str, localizacao: str):
        busca = f"{endereco} {localizacao}".lower()
        encontrados = []

        for lugar in self.ESTABELECIMENTOS:
            rua = lugar["endereco"].split(",")[0].lower()
            bairro = lugar["bairro"].lower()
            if rua in busca or bairro in busca:
                encontrados.append(lugar)

        if encontrados:
            self.__estabelecimento = encontrados[0]["nome"]  # guarda o mais próximo

        return encontrados

    def mostra_relatorio(self, km_inicial: float, km_final: float, tempo_exe: str):

        self.km_final = km_final
        self.tempo_exec = tempo_exec
        relatorio = f"Treino de {self.nome}:\n"
        relatorio += f"Localização: {self.localizacao}\n"
        relatorio += f"Distância percorrida: {self.km_final - self.km_inicial:.2f} km\n"
        relatorio += f"Tempo de execução: {self.tempo_exec}\n"
        if self.__estabelecimento:
            relatorio += f"Estabelecimento mais próximo: {self.__estabelecimento}\n"
        else:
            relatorio += "Nenhum estabelecimento próximo encontrado.\n"
        return relatorio

    def classifica_ritmo(self):
        distancia = (self.km_final - self.km_inicial)
        pace = self.tempo_exec / distancia  # tempo por km
        