from categoria_produto import CategoriaProduto
from cliente import Cliente


class Produto:
    def __init__(self, codigo: int, descricao: str, categoria_produto: CategoriaProduto):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__categoria_produto = categoria_produto
        self.__quantidade = 0
        self.__preco_unitario = None
        self.__cliente = None


    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int):
        self.__quantidade = quantidade

    @property
    def preco_unitario(self):
        return self.__preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, preco_unitario: int):
        self.__preco_unitario = preco_unitario

    def preco_total(self):
        return float(self.__quantidade * self.__preco_unitario)

    ''''métodos com as classes CategoriaProduto e Cliente '''

    @property
    def categoria_produto(self):
        return self.__categoria_produto

    @categoria_produto.setter
    def categoria_produto(self, categoria_produto: CategoriaProduto):
        if isinstance(categoria_produto, CategoriaProduto):
            self.__categoria_produto = categoria_produto

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente



















