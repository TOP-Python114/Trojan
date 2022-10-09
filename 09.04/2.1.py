
# ДОБАВИТЬ: документацию класса
class Director:
    # ДОБАВИТЬ: аннотации типов
    def __init__(self, fullname):
        self.fullname = fullname

    def __str__(self):
        return self.fullname


# ДОБАВИТЬ: документацию класса
class FilmCard:
    # ДОБАВИТЬ: аннотации типов
    def __init__(self, id_, name, year, genre, country, fullname):
        self.name = name
        self.year = year
        self.genre = genre
        self.country = country
        # ИСПРАВИТЬ: стоит перенести создание экземпляра Director в код фабрики
        self.director = Director(fullname)
        self.id = id_
        # ДОБАВИТЬ: хотелось бы больше полей — включая следующий/предыдущий фильм во франшизе

    def __str__(self):
        return f"Информация о фильме №{self.id}:\n" \
               f" Название: {self.name}\n" \
               f" Год производства: {self.year}\n" \
               f" Жанр: {self.genre}\n" \
               f" Страна: {self.country}\n" \
               f" Режиссер: {self.director}"


# ДОБАВИТЬ: документацию класса
class FactoryFilm:
    def __init__(self):
        # КОММЕНТАРИЙ: помещение этого атрибута в экземпляр означает, что можно будет создать ещё один экземпляр фабрики (например, ff2), и карточки, созданные с его помощью, будут нумероваться с нуля — это то, что необходимо понимать и иметь в виду
        self.id = 0

    # ДОБАВИТЬ: аннотации типов
    def create_cardfilm(self, name, year, genre, country, director):
        self.id += 1
        return FilmCard(self.id, name, year, genre, country, director)


ff = FactoryFilm()
film1 = ff.create_cardfilm('"Невидимый гость"', 2016, 'триллер', 'Испания', 'Ориол Паоло')
film2 = ff.create_cardfilm('"Лучшее предложение"', 2012, 'драма', 'Италия', 'Джузеппе Торнаторе')
film3 = ff.create_cardfilm('"Искупление"', 2007, 'драма', 'Великобритания', 'Джо Райт')
film4 = ff.create_cardfilm('"Гнев человеческий"', 2021, 'боевик', 'Великобритания', 'Гай Ричи')
film5 = ff.create_cardfilm('"Джентельмены"', 2019, 'комедия', 'Великобритания', 'Гай Ричи')

print(film1, film2, film3, film4, film5, sep='\n', end='\n\n')


# stdout:
"""
Информация о фильме №1:
 Название: "Невидимый гость"
 Год производства: 2016
 Жанр: триллер
 Страна: Испания
 Режиссер: Ориол Паоло
Информация о фильме №2:
 Название: "Лучшее предложение"
 Год производства: 2012
 Жанр: драма
 Страна: Италия
 Режиссер: Джузеппе Торнаторе
Информация о фильме №3:
 Название: "Искупление"
 Год производства: 2007
 Жанр: драма
 Страна: Великобритания
 Режиссер: Джо Райт
Информация о фильме №4:
 Название: "Гнев человеческий"
 Год производства: 2021
 Жанр: боевик
 Страна: Великобритания
 Режиссер: Гай Ричи
Информация о фильме №5:
 Название: "Джентельмены"
 Год производства: 2019
 Жанр: комедия
 Страна: Великобритания
 Режиссер: Гай Ричи
 """


# ИТОГ: очень хорошо, ещё бы не игнорировали часть задания по документации и аннотациям — 10/12


# СДЕЛАТЬ: жду остальные задачи
