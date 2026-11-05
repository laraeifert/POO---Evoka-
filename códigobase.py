class Pessoa:

    def __init__(self, nome: str, email: str, contato_emerg: int = 192):
        #Atributos públicos (+), recebidos na criação do objeto
        self.nome = nome
        self.email = email

        #Atributos publicos (+), não recebidos na criação do objeto
        self.idade = None
        self.endereco = None
        self.cpf = str()
        self.treinos = list()
        self.estabelecimentos = list() 

        #Atributo privado (-), recebido na criação do objeto
        self.__contato_emerg = contato_emerg

    def set_contato_emerg(self, contato_emerg: int):
        #Atributo privado (-), alterado após a criação do objeto
        self.__contato_emerg = contato_emerg
    
    def ver_contato_emerg(self):
        #Atributo privado (-), acessado após a criação do objeto
        return self.__contato_emerg

class Estabelecimento:
    def __init__(self, nome: str, endereco: str,):
        #Atributos públicos (+)
        self.nome = nome
        self.endereco = endereco
    def set_cnpj(self, cnpj: int):
        #Atributos Protegidos (#)
        self._cnpj = cnpj
    def set_produtos(self, produtos: str):
        #Atributos privados (-)
        self.__produtos = produtos
    def ver_produtos(self):
        return self.__produtos