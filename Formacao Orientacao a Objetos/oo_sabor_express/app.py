from models.restaurante import Restaurante
from models.menu.drink import Drink
from models.menu.plate import Plate

restaurante_praca = Restaurante('praça', 'Gourmet')
drink_juice = Drink("Abacaxi", 10.0, "Grande")
drink_juice.apply_discount()
plate_bean = Plate("Feijoada", 25.0, "Prato de feijoada")
plate_bean.apply_discount()
restaurante_praca.append_item_on_menu(drink_juice)
restaurante_praca.append_item_on_menu(plate_bean)


def main():
    restaurante_praca.display_menu


if __name__ == '__main__':
    main()
