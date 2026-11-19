class Corrida(Treinos):
    def __init__(self, localizacao: str, km_inicial: float, nome: TipoTreino):
        #Herança da classe Treinos
        super().__init__(localizacao, km_inicial, nome)
        #Atributos só da corrida
        self.velocidade_media = None
        self.frequencia_cardiaca = None

    def calcula_ritmo(self):
        #Ritmo = km_inicial / tempo (minutos)
        if self.km_inicial is None or self.tempo_exe is None:
            raise ValueError("km_inicial e tempo devem ser definidos para calcular o ritmo.")
        distancia = self.km_final - self.km_inicial
        if distancia <= 0:
            raise ValueError("km_final deve ser maior que km_inicial.")
        minutos = self.tempo_exe.total_seconds() / 60
        return minutos / distancia
    

class Caminhada(Treinos):
    def __init__(self, localizacao: str, km_inicial: float, nome: TipoTreino):
        #Herança da classe Treinos
        super().__init__(localizacao, km_inicial, nome)
        #Atributos só da caminhada
        self.passos = None
        self.inclinacao = None

    def calcula_passos_por_minuto(self):
        if self.km_final is None or self.tempo_exe is None:
            raise ValueError("km_final e tempo_exe devem ser definidos para calcular o ritmo.")
        minutos = self.tempo_exe.total_seconds() / 60
       if minutos <= 0:
            raise ValueError("tempo_exe deve ser maior que zero.")
        return self.passos / minutos