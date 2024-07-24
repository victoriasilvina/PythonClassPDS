from filmes import Filmes

class Magico(Filmes):
    def __init__(self, titulo, ano, autor):
        self._categoria = "Filme de Magia"
        self.__codigo = "0912"
        super().__init__(titulo, ano, autor, self._categoria, self.__codigo)

class Acao(Filmes):
    def __init__(self, titulo, ano, autor):
        self._categoria = "Filme de Ação"
        self.__codigo = "1209"
        super().__init__(titulo, ano, autor, self._categoria, self.__codigo)
    
