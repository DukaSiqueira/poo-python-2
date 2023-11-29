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


class Playlist:
    def __init__(self, nome, programas):
        self.mome = nome
        self.__programas = programas

    def __getitem__(self, item):
        return self.__programas[item]

    @property
    def list_programs(self):
        return self.__programas

    def __len__(self):
        return len(self.__programas)


filme = Filme("doutor estranho", 2013, 260)
filme.dar_like()
filme.dar_like()
filme.dar_like()

filme2 = Filme("homem aranha sem volta pra casa", 2022, 280)
filme2.dar_like()
filme2.dar_like()
filme2.dar_like()
filme2.dar_like()
filme2.dar_like()


serie = Serie("dr. house", 2012, 8)
serie.dar_like()
serie.dar_like()
serie.dar_like()
serie.dar_like()
serie.dar_like()

serie2 = Serie("wanda vision", 2012, 8)
serie2.dar_like()
serie2.dar_like()
serie2.dar_like()
serie2.dar_like()
serie2.dar_like()

programacao = [filme, serie, serie2, filme2]

playlist = Playlist("Programas de Segunda", programacao)

print(playlist.__len__())
for programa in playlist:
    print(programa)
