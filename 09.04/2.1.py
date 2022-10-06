
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

    def create_person(self, name, year, genre, country, obj_producer):
        self.id += 1
        return FilmCard(self.id, name, year, genre, country, obj_producer)


pf = FactoryFilm()
film1 = pf.create_person('"Невидимый гость"', 2016, 'триллер', 'Испания', 'Ориол Паоло')
film2 = pf.create_person('"Лучшее предложение"', 2012, 'драма', 'Италия', 'Джузеппе Торнаторе')
film3 = pf.create_person('"Искупление"', 2007, 'драма', 'Великобритания', 'Джо Райт')
film4 = pf.create_person('"Гнев человеческий"', 2021, 'боевик', 'Великобритания', 'Гай Ричи')
film5 = pf.create_person('"Джентельмены"', 2019, 'комедия', 'Великобритания', 'Гай Ричи')

print(film1, film2, film3, film4, film5, sep='\n', end='\n\n')

