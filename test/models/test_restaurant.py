from src.models.restaurant import Restaurant


class TestRestaurant:

    def test_describe_restaurant(self):
        #Setup
        restaurante = Restaurant("Casa de Taipa", "Comida Nordestina")
        resultado_esperado = "Esse restaturante chama: Casa De Taipa and serve: Comida Nordestina, está servindo: 0 consumidores desde que está aberto."
        #Chamada
        resultado = restaurante.describe_restaurant()
        #Avaliação
        assert resultado == resultado_esperado

    def test_open_restaurant(self):
        # Setup
        restaurante = Restaurant("Casa De Taipa", "Comida Nordestina")
        resulato_esperado = "Casa De Taipa agora está aberto!"
        # Chamada
        resultado = restaurante.open_restaurant()
        # Avaliação
        assert resultado == resulato_esperado

    def test_open_restaurant_ja_esta_aberto(self):
        # Setup
        restaurante = Restaurant("Casa De Taipa", "Comida Nordestina")
        resulato_esperado = "Casa De Taipa já está aberto!"
        restaurante.open = True# Passando True para que na chamada do metodo o retaurante já esteja aberto
        # Chamada
        resultado = restaurante.open_restaurant()
        # Avaliação
        assert resultado == resulato_esperado

    def test_close_restaurant(self):
        # Setup
        restaurante = Restaurant("Casa De Taipa", "Comida Nordestina")
        resulato_esperado = "Casa De Taipa agora está fechado!"
        restaurante.open = True
        # Chamada
        resultado = restaurante.close_restaurant()
        # Avaliação
        assert resultado == resulato_esperado

    def test_close_restaurant_ja_esta_fechado(self):
        # Setup
        restaurante = Restaurant("Casa De Taipa", "Comida Nordestina")
        resulato_esperado = "Casa De Taipa já está fechado!"
        # Chamada
        resultado = restaurante.close_restaurant()
        # Avaliação
        assert resultado == resulato_esperado

    def test_set_number_served(self):
        # Setup
        restaurante = Restaurant("Casa De Taipa", "Comida Nordestina")
        restaurante.open = True # Abrindo o restaurante para adicionar pessoas atendidas
        resultado_esperado = 5
        # Chamada
        resultado = restaurante.set_number_served(5)
        # Avaliação
        assert resultado == resultado_esperado

    def test_set_number_served_fechado(self):
        # Setup
        restaurante = Restaurant("Casa De Taipa", "Comida Nordestina")
        resultado_esperado = "Casa De Taipa está fechado!"
        # Chamada
        resultado = restaurante.set_number_served(5)
        # Avaliação
        assert resultado == resultado_esperado

    def test_increment_number_served(self):
        # Setup
        restaurante = Restaurant("Casa De Taipa", "Comida Nordestina")
        restaurante.open = True # Abrindo o restaurante para adicionar pessoas atendidas
        restaurante.number_served = 1
        resultado_esperado = 6
        # Chamada
        resultado = restaurante.increment_number_served(5)
        # Avaliação
        assert resultado == resultado_esperado

    def test_increment_number_served_estando_fechado(self):
        # Setup
        restaurante = Restaurant("Casa De Taipa", "Comida Nordestina")
        #restaurante.open = True  # Abrindo o restaurante para adicionar pessoas atendidas
        resultado_esperado = "Casa De Taipa está fechado!"
        # Chamada
        resultado = restaurante.increment_number_served(5)
        # Avaliação
        assert resultado == resultado_esperado
