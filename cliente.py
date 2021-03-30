
class Cliente:
    def __init__(self, nome: str, fone: str):
        self.__nome = nome
        self.__fone = fone

    '''recuperar o dado do atributo nome'''
    @property
    def nome(self):
        return self.__nome

    '''alterar o atributo nome'''
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    ''''recuperar o dado do atributo fone'''
    @property
    def fone(self):
        return self.__fone

    ''''alterar o atributo fone'''
    @fone.setter
    def fone(self, fone: str):
        self.__fone = fone

