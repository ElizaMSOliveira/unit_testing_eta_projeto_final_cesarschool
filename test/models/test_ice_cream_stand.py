from src.models.ice_cream_stand import IceCreamStand


class Test_ice_crean:

    def test_flavors_available_success(self):
        ice_crean = IceCreamStand("Casa de Taipa", "Sorveteria")
        resultado_esperado = "['Morango', 'Abacaxi', 'Chocolate']"
        resultado = ice_crean.flavors_available()
        assert resultado == resultado_esperado

    # PARA FAZER ESSSE TESTE RETIREI OS ITENS DA LISTA
    def test_flavors_available_failed(self):
        ice_crean = IceCreamStand("Casa de Taipa", "Sorveteria")
        resultado_esperado = "Estamos sem estoque atualmente!"
        resultado = ice_crean.flavors_available()
        assert resultado == resultado_esperado

    def test_find_flavor_estando_na_lista(self):
        ice_crean = IceCreamStand("Casa de Taipa", "Sorveteria")
        resultado_esperado = "Temos no momento Morango!"
        resultado = ice_crean.find_flavor("Morango")
        assert resultado == resultado_esperado

    def test_find_flavor_não_estando_na_lista(self):
        ice_crean = IceCreamStand("Casa de Taipa", "Sorveteria")
        resultado_esperado = "Não temos no momento Flocos!"
        resultado = ice_crean.find_flavor("Flocos")
        assert resultado == resultado_esperado

    # PARA FAZER ESSSE TESTE RETIREI OS ITENS DA LISTA
    def test_find_flavor_failed(self):
        ice_crean = IceCreamStand("Casa de Taipa", "Sorveteria")
        resultado_esperado = "Estamos sem estoque atualmente!"
        resultado = ice_crean.find_flavor("Pitanga")
        assert resultado == resultado_esperado

    def test_add_flavor_success(self):
        ice_crean = IceCreamStand("Casa de Taipa", "Sorveteria")
        resultado_esperado = "Limão adicionado ao estoque!"
        resultado = ice_crean.add_flavor("Limão")
        assert resultado == resultado_esperado

    def test_add_flavor_ja_existente(self):
        ice_crean = IceCreamStand("Casa de Taipa", "Sorveteria")
        resultado_esperado = "Sabor já disponivel!"
        resultado = ice_crean.add_flavor("Abacaxi")
        assert resultado == resultado_esperado

