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

    def __str__(self):
        return f'Nome: {self.nome}  Ano: {self.ano} Likes: {self.likes}'


class Filme (Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome}  Ano: {self.ano} Duração: {self.duracao} Likes: {self.likes}'


class Serie (Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome}  Ano: {self.ano} Temporadas: {self.temporadas} Likes: {self.likes}'


filme = Filme("doutor estranho", 2013, 260)
filme.dar_like()
filme.dar_like()
filme.dar_like()


serie = Serie("dr. house", 2012, 8)
serie.dar_like()
serie.dar_like()
serie.dar_like()
serie.dar_like()
serie.dar_like()

programacao = [filme, serie]

for programa in programacao:
    print(programa)
