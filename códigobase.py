class Pessoa:
    def __init__(self, nome: str, email: str, contato_emerg: int = 192):
        #Atributos públicos (+)
        self.nome = nome
        self.email = email
        self.contato_emerg = contato_emerg
    def set_contato_emerg(self, contato_emerg: int):
        #Atributo privado (-)
        self.__contato_emerg = contato_emerg
    #Atributos publicos (+)    
    self.idade = idade 
    self.endereco = endereco
    self.cpf = cpf 


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