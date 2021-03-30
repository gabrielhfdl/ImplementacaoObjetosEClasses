
class CategoriaProduto:
    def __init__(self, titulo: str):
        self.__titulo = titulo

    ''''recuperar o titulo do produto '''
    @property
    def titulo(self):
        return self.__titulo

    ''''alterar o titulo do produto'''
    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo
