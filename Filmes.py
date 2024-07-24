class Filmes:
    def __init__(self, titulo, ano, autor, categoria, codigo):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor
        self._categoria = categoria
        self.__codigo = codigo
    
    def informacoes(self):
        print("")
        print(f"TÍTULO DO FILME..: {self.titulo}")
        print(f"ANO DE LANÇAMENTO: {self.ano}")
        print(f"NOME DO AUTOR....: {self.autor}")
    
    def exibir_categoria(self):
        print(f"Categoria: {self._categoria}")

    def exibir_codigo(self):
        print(f"Código: {self.__codigo}")
        
        print("---------------------------------------")
