
class Producer:
    def __init__(self, fullname):
        self.fullname = fullname
    def __str__(self):
        return self.fullname

class FilmCard:
    def __init__(self, id_, name, year, genre, country, fullname):
        self.name = name
        self.year = year
        self.genre = genre
        self.country = country
        self.obj_producer = Producer(fullname)
        self.id = id_

    def __str__(self):
        return f"Информация о фильме №{self.id}:\n Название: {self.name}\n Год производства: {self.year}\n Жанр: {self.genre}\n Страна: {self.country}\n Режиссер: {self.obj_producer}"

class FactoryFilm:
    def __init__(self):
        self.id = 0

    def create_cardfilm(self, name, year, genre, country, obj_producer):
        self.id += 1
        return FilmCard(self.id, name, year, genre, country, obj_producer)


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
