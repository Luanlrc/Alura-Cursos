from models.avaliacao import Avaliacao
from models.menu.item_menu import ItemMenu


class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._name = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._menu = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._name} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._name.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    def append_item_on_menu(self, item):
        if isinstance(item, ItemMenu):
            self._menu.append(item)

    @property
    def display_menu(self):
        print(f"Cardapio do restaurante {self._name}\n")
        for i, item in enumerate(self._menu, start=1):
            if hasattr(item, "description"):
                mensagem_plate = f"{i}. Nome:{item._name} | Preço:{item._value} | Descrição: {item.description}"
                print(mensagem_plate)
            else:
                mensagem_drink = f"{i}. Nome:{item._name} | Preço:{item._value} | Descrição: {item.size}"
                print(mensagem_drink)
