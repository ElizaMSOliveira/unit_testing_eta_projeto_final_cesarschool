from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""
    def __init__(self, restaurant_name, cuisine_type):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors_list = ['Morango', 'Abacaxi', 'Chocolate']

        # TODOS OS PRINT FORAM TROCADOS POR RETURN
        # CORRIGIDO BUGS DE IDENTAÇÃO
    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        if self.flavors_list:
            #return ("\nNo momento temos os seguintes sabores de sorvete disponíveis:") #BUG Não é possivel ter 2 retorno
            for flavor in self.flavors_list:
                return f"{self.flavors_list}"
        else: #TESTE REALIZADO RETIRANDO OS ITENS DA LISTA
            return ("Estamos sem estoque atualmente!")

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        if self.flavors_list: # O self.flavors FOI SUBSTITUIDO POR self.flavors_list ONDE TEMOS ALISTA COM OS SABORES
            if flavor in self.flavors_list: # TAMBEM HOUVE A SUBSTIRUIÇÃO PARA PERCORRER A LISTA DE SABORES
                return (f"Temos no momento {flavor}!") #O self.flavors FOI SUBSTITUIDO POR flavor RETORNANDO A CONFIRMAÇÃO.
            else:
               return f"Não temos no momento {flavor}!"#O self.flavors FOI SUBSTITUIDO POR flavor RETORNANDO A CONFIRMAÇÃO.
        else: #TESTE REALIZADO RETIRANDO OS ITENS DA LISTA
            return ("Estamos sem estoque atualmente!")

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        if self.flavors_list:# O self.flavors FOI SUBSTITUIDO POR self.flavors_list ONDE TEMOS ALISTA COM OS SABORES
            if flavor in self.flavors_list:
                return ("Sabor já disponivel!")
            else:
                self.flavors_list.append(flavor)
                return(f"{flavor} adicionado ao estoque!")
        else:
            return("Estamos sem estoque atualmente!")
