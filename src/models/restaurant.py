class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""  # retur no lugar de print e ajustes de retorno
        # retunr no lugar de print
        return f"Esse restaturante chama: {self.restaurant_name} and serve: {self.cuisine_type}, está servindo: {self.number_served} consumidores desde que está aberto."

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            self.open = True  # Recebendo True para ser aberto
            self.number_served = 2  # Adicionando valor positivo a quantidade de cliantes ja que acabamos de abrir, apesar que esse não faz diferença pro metodo
            return f"{self.restaurant_name} agora está aberto!"# retunr no lugar de print
        else:
            return f"{self.restaurant_name} já está aberto!"# retunr no lugar de print

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if not self.open:
            #self.number_served = 0 # Se ta fechado não faz sentido atribuir valor
            return f"{self.restaurant_name} já está fechado!"# retunr no lugar de print
        else:
            self.open = False # Fechando o restaurante já que o metodo para ser testado recebeu ele aberto(True)
            return f"{self.restaurant_name} agora está fechado!"# retunr no lugar de print

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        if self.open:
            self.number_served = total_customers
            return self.number_served # Adicionando o retorno
        else:
            return f"{self.restaurant_name} está fechado!"# retunr no lugar de print

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        if self.open:
            self.number_served += more_customers # Incrementando (+=) ao invés de atribuir(=)
            return self.number_served # Adicionado o retorno
        else:
            return f"{self.restaurant_name} está fechado!"# retunr no lugar de print
