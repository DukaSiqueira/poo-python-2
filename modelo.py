class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1


class Filme (Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie (Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


filme = Filme("doutor estranho", 2013, 260)
filme.dar_like()
filme.dar_like()
filme.dar_like()
print("Nome: {} Ano: {} Duração: {} Likes: {}".
      format(filme.nome, filme.ano, filme.duracao, filme.likes))


serie = Serie("dr. house", 2012, 8)
serie.dar_like()
serie.dar_like()
serie.dar_like()
serie.dar_like()
serie.dar_like()
print("Nome: {} Ano: {} Temporadas: {} Likes: {}".
      format(serie.nome, serie.ano, serie.temporadas, serie.likes))
