from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from sys import path
from json import load as jload


# ИСПОЛЬЗОВАТЬ: когда данных много, то можно не стесняться выносить их в отдельный файл
db_path = Path(path[0]) / 'dishes.json'


# ИСПОЛЬЗОВАТЬ: есть такая классная штука: дата-классы — прям как для этого случая придуманы
@dataclass
class Dish(ABC):
    # ИСПОЛЬЗОВАТЬ: литерал со строкой документации должен помещать непосредственно под заголовком класса/метода/функции — иначе этот литерал не будет записан в атрибут __doc__ класса/метода/функции
    """Абстрактный класс, реализующий описание блюда"""
    dish_name: str
    specification: str
    ingredient_list: str
    weight: int
    price: float
    country: str

    @abstractmethod
    def dish(self):
        pass

    def __str__(self):
        return f"Название блюда: {self.dish_name}\n" \
               f"Описание: {self.specification}\n" \
               f"Ингредиенты: {self.ingredient_list}\n" \
               f"Граммовка блюд: {self.weight}\n" \
               f"Цена: {self.price}\n" \
               f"Традиционная кухня: {self.country}"


# КОММЕНТАРИЙ: а комментарии, тем более короткие, пишите как комментарии, не как литералы — первые игнорируются интерпретатором, а вторые вычисляются
# Классы, реализующие описание конкретного блюда
class CabbageSoup(Dish):
    def dish(self):
        print('Закажите Щи')

class Minestrone(Dish):
    def dish(self):
        print('Закажите Минестроне')

class MisoSoup(Dish):
    def dish(self):
        print('Закажите Мисо суп')

# ИСПОЛЬЗОВАТЬ: для имён классов используйте регистр CamelCase, а не Title_Snake_Case
class SushiTuna(Dish):
    def dish(self):
        print('Закажите Суши Туна')

class Pepperonate(Dish):
    def dish(self):
        print('Закажите Пеппероната')

class Meatballs(Dish):
    def dish(self):
        print('Закажите Тефтели')

class Vinaigrette(Dish):
    def dish(self):
        print('Закажите Винегрет')

class Aranchini(Dish):
    def dish(self):
        print('Закажите Аранчини')

class Konji(Dish):
    def dish(self):
        print('Закажите Конджи')


class AbstractDishFactory(ABC):
    """Абстрактный класс, реализующий набор ресторанных блюд"""
    @abstractmethod
    def serving_first_course(self):
        pass

    @abstractmethod
    def serving_second_course(self):
        pass

    @abstractmethod
    def serving_snack(self):
        pass


class RussianCuisineFactory(AbstractDishFactory):
    """Класс, реализующий блюда русской кухни"""
    # ИСПОЛЬЗОВАТЬ: вот так, пожалуй, будет удобнее
    def __init__(self):
        with open(db_path, encoding='utf-8') as filein:
            dishes = jload(filein)
        self.first = dishes['CabbageSoup']
        self.second = dishes['Meatballs']
        self.snack = dishes['Vinaigrette']

    def serving_first_course(self):
        return CabbageSoup(**self.first)

    def serving_second_course(self):
        return Meatballs(**self.second)

    def serving_snack(self):
        return Vinaigrette(**self.snack)


class AsianCuisineFactory(AbstractDishFactory):
    """Класс, реализующий блюда азиатской кухни"""
    def __init__(self):
        with open(db_path, encoding='utf-8') as filein:
            dishes = jload(filein)
        self.first = dishes['MisoSoup']
        self.second = dishes['SushiTuna']
        self.snack = dishes['Konji']

    def serving_first_course(self):
        return MisoSoup(**self.first)

    def serving_second_course(self):
        return SushiTuna(**self.second)

    def serving_snack(self):
        return Konji(**self.snack)


class ItalianCuisineFactory(AbstractDishFactory):
    """Класс, реализующий блюда итальянской кухни"""
    def __init__(self):
        with open(db_path, encoding='utf-8') as filein:
            dishes = jload(filein)
        self.first = dishes['Minestrone']
        self.second = dishes['Pepperonate']
        self.snack = dishes['Aranchini']

    def serving_first_course(self):
        return Minestrone(**self.first)

    def serving_second_course(self):
        return Pepperonate(**self.second)

    def serving_snack(self):
        return Aranchini(**self.snack)


# КОММЕНТАРИЙ: здесь уже не фабрика — это управляющий класс, который вероятнее всего будет вообще находиться в другом модуле — код верхнего уровня, иначе говоря
class FactoryDish:
    """Фабрика блюд"""
    def __init__(self, factory: AbstractDishFactory):
        self.fac = factory

    def create_menu(self):
        first = self.fac.serving_first_course()
        second = self.fac.serving_second_course()
        snack = self.fac.serving_snack()
        first.dish()
        second.dish()
        snack.dish()


def create_factory(cuisine: str) -> AbstractDishFactory:
    factory_dict = {
        "russia": RussianCuisineFactory,
        "asia": AsianCuisineFactory,
        "italy": ItalianCuisineFactory
    }
    return factory_dict[cuisine]()


if __name__ == '__main__':
    answer = input('Какая кухня вас интересует? [russia/asia/italy]\n')
    nc = create_factory(answer)
    fd = FactoryDish(nc)
    fd.create_menu()


# stdout:
"""
Заказываю Щи
Заказываю Тефтели
Заказываю Винегрет
"""


# ИТОГ: отлично — 11/12


# СДЕЛАТЬ: всё ещё жду первую часть задания =)
