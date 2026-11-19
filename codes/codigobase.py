from enum import Enum
from datetime import timedelta

class Pessoa:

    def __init__(self, nome: str, email: str, contato_emerg: int = 192):
        # Atributos públicos (+), recebidos na criação do objeto
        self.nome = nome
        self.email = email

        # Atributos públicos (+), não recebidos na criação do objeto
        self.idade = None
        self.endereco = None
        self.cpf = None
        self.treinos = list()
        self.estabelecimentos = list()

        # Atributo privado (-): o nome começa com dois underlines
        self.__contato_emerg = contato_emerg

    def set_contato_emerg(self, contato_emerg: int):
        self.__contato_emerg = contato_emerg

    def ver_contato_emerg(self):
        return self.__contato_emerg

class Estabelecimento:

    def __init__(self, nome: str, endereco: str):
        # Atributos públicos (+)
        self.nome = nome
        self.endereco = endereco

        # Atributo protegido (#): o nome começa com um underline
        self._cnpj = None

        # Atributo privado (-): o nome começa com dois underlines
        self.__produtos = None

    def set_cnpj(self, cnpj: str):
        self._cnpj = cnpj

    def set_produtos(self, produtos: str):
        self.__produtos = produtos

    def ver_produtos(self):
        return self.__produtos

class TipoTreino(Enum):
    CORRIDA = "Corrida"
    CAMINHADA = "Caminhada"

class Treinos:

    # Estabelecimentos cadastrados no sistema (onde a busca é feita)
    ESTABELECIMENTOS = [
        Estabelecimento("Padaria Pão Quente", "Av. Guilherme Schell, 100"),
        Estabelecimento("Academia Corpo em Forma", "Av. Guilherme Schell, 250"),
        Estabelecimento("Farmácia Saúde", "Rua Tiradentes, 45"),
    ]

    def __init__(self, localizacao: str, km_inicial: float, nome: TipoTreino):
        self.nome = nome
        self.localizacao = localizacao
        self.km_inicial = km_inicial
        self.km_final = None
        self.tempo_exec = None   # vai ser um timedelta
        self.pessoa = None       # a Pessoa dona do treino
        self.__estabelecimentos = list()   # atributo privado

    def procura_estabelecimento(self, endereco: str, localizacao: str):
        busca = f"{endereco} {localizacao}".lower()
        encontrados = []

        for lugar in self.ESTABELECIMENTOS:
            rua = lugar.endereco.split(",")[0].lower()
            if rua in busca:
                encontrados.append(lugar)

        # guarda todos os encontrados no treino (e na pessoa, se houver)
        for lugar in encontrados:
            if lugar not in self.__estabelecimentos:
                self.__estabelecimentos.append(lugar)
            if self.pessoa and lugar not in self.pessoa.estabelecimentos:
                self.pessoa.estabelecimentos.append(lugar)

        return encontrados

    # MÉTODO PRIVADO
    def __calcula_distancia(self):
        return self.km_final - self.km_inicial

    def mostra_relatorio(self, km_final: float, tempo_exec):
        self.km_final = km_final
        self.tempo_exec = tempo_exec

        relatorio = f"Treino de {self.nome.value}"
        if self.pessoa:
            relatorio += f" - {self.pessoa.nome}"
        relatorio += "\n"
        relatorio += f"Localização: {self.localizacao}\n"
        relatorio += f"Distância percorrida: {self.__calcula_distancia():.2f} km\n"
        relatorio += f"Tempo de execução: {self.tempo_exec}\n"
        relatorio += f"Intensidade: {self.classifica_ritmo()}\n"
        if self.__estabelecimentos:
            nomes = ", ".join(e.nome for e in self.__estabelecimentos)
            relatorio += f"Estabelecimentos no percurso: {nomes}\n"
        else:
            relatorio += "Nenhum estabelecimento próximo encontrado.\n"
        return relatorio

    def classifica_ritmo(self):
        # Será sobrescrito pelas classes filhas (POLIMORFISMO)
        return "Sem classificação"


class Corrida(Treinos):

    def __init__(self, localizacao: str, km_inicial: float):
        super().__init__(localizacao, km_inicial, TipoTreino.CORRIDA)

        # Atributos só da corrida
        self.velocidade_media = None
        self.frequencia_cardiaca = None

    def calcula_ritmo(self):
        # Ritmo = minutos por km
        distancia = self.km_final - self.km_inicial
        if distancia <= 0:
            raise ValueError("km_final deve ser maior que km_inicial.")
        minutos = self.tempo_exec.total_seconds() / 60
        return minutos / distancia
    
    def classifica_ritmo(self):
        ritmo = self.calcula_ritmo()
        if ritmo < 5:
            return "Rápido"
        elif ritmo < 7:
            return "Moderado"
        return "Leve"

class Caminhada(Treinos):

    def __init__(self, localizacao: str, km_inicial: float):
        super().__init__(localizacao, km_inicial, TipoTreino.CAMINHADA)

        # Atributos só da caminhada
        self.passos = None
        self.inclinacao = None

    def calcula_passos_por_minuto(self):
        if self.passos is None or self.tempo_exec is None:
            raise ValueError("passos e tempo_exec devem ser definidos.")
        minutos = self.tempo_exec.total_seconds() / 60
        if minutos <= 0:
            raise ValueError("tempo_exec deve ser maior que zero.")
        return self.passos / minutos

    def classifica_ritmo(self):
        ppm = self.calcula_passos_por_minuto()
        if ppm >= 120:
            return "Intenso"
        elif ppm >= 100:
            return "Moderado"
        return "Leve"

def main():
    # Objetos Pessoa
    ana = Pessoa("Ana", "ana@email.com")
    ana.set_contato_emerg(51999990000)
    bruno = Pessoa("Bruno", "bruno@email.com")

    # Objeto Estabelecimento
    mercado = Estabelecimento("Mercado Central", "Rua Itália, 10")
    mercado.set_cnpj("12.345.678/0001-90")
    mercado.set_produtos("Frutas, pães, bebidas")

    # Corrida da Ana (associação Pessoa <-> Treino)
    corrida = Corrida("Av. Guilherme Schell", 0)
    corrida.frequencia_cardiaca = 160
    ana.treinos.append(corrida)
    corrida.pessoa = ana
    corrida.procura_estabelecimento("Av. Guilherme Schell", "Centro")

    # Caminhada do Bruno
    caminhada = Caminhada("Rua Tiradentes", 0)
    caminhada.passos = 5200
    caminhada.inclinacao = 2
    bruno.treinos.append(caminhada)
    caminhada.pessoa = bruno
    caminhada.procura_estabelecimento("Rua Tiradentes", "Centro")

    # Polimorfismo:
    print(corrida.mostra_relatorio(5.0, timedelta(minutes=28)))
    print(f"Ritmo: {corrida.calcula_ritmo():.2f} min/km")
    print(f"Frequência cardíaca: {corrida.frequencia_cardiaca} bpm\n")

    print(caminhada.mostra_relatorio(4.0, timedelta(minutes=48)))
    print(f"Passos por minuto: {caminhada.calcula_passos_por_minuto():.0f}\n")

    print("Contato de emergência da Ana:", ana.ver_contato_emerg())
    print("Estabelecimentos da Ana:", [e.nome for e in ana.estabelecimentos])
    print("Mercado:", mercado.nome, "| Produtos:", mercado.ver_produtos())


if __name__ == "__main__":
    main()