from abc import ABC, abstractmethod


# Passenger & Cargo Carriers
class Carrier(ABC):
    """Абстрактный класс, реализующий назначение самолета. Мост."""
    @abstractmethod
    def carry_military(self, items):
        pass

    @abstractmethod
    def carry_commercial(self, items):
        pass


class Passenger(Carrier):
    """Класс пассажирcкого самолета"""
    def carry_military(self, items):
        """Выводит описание военного самолета, перевозящего пассажиров"""
        return f'Военный самолет перевозит {items} человек'

    def carry_commercial(self, items):
        """Выводит описание коммерческого самолета, перевозящего пассажиров"""
        return f'Коммерческий самолет перевозит {items} пассажиров'


class Cargo(Carrier):
    """Класс грузового самолета"""
    def carry_military(self, items):
        """Выводит описание военного самолета, перевозящего грузы"""
        return f'Военный самолет перевозит {items} боеприпасов'

    def carry_commercial(self, items):
        """Выводит описание коммерческого самолета, перевозящего грузы"""
        return f'Коммерческий самолет перевозит {items} товаров'


# Military & Commercial Planes
class Plane(ABC):
    """Абстрактный класс, реализующий сферу использования самолета"""
    @abstractmethod
    def display_description(self):
        pass

    @abstractmethod
    def add_objects(self, new_objects):
        pass


class Military(Plane):
    """Класс военного самолета"""
    # ДОБАВИТЬ: аннотацию objects
    def __init__(self, carrier: Carrier, objects):
        self.carrier = carrier
        self.objects = objects

    def display_description(self):
        """Выводит описание военного самолета"""
        # УДАЛИТЬ: первая строка бесполезна, дублирование кода
        self.carrier.carry_military(self.objects)
        return f'{self.carrier.carry_military(self.objects)}'

    def add_objects(self, new_objects):
        """Добавляет пассажиров/грузы, перевозка которых осуществляется военным самолетом"""
        # ИСПРАВИТЬ: опасно использовать сложение/конкатенацию, когда не знаете типы — вдруг здесь кортеж с числом кто-то сложить попытается?
        self.objects += new_objects


class Commercial(Plane):
    """Класс коммерческого самолета"""
    # КОММЕНТАРИЙ: если реализации методов не отличаются, то лучше прописать эту реализацию в базовом классе — Python позволяет нам прописывать обычные наследуемые методы и в абстрактном классе
    def __init__(self, carrier: Carrier, objects):
        self.carrier = carrier
        self.objects = objects

    def display_description(self):
        """Выводит описание коммерческого самолета"""
        # УДАЛИТЬ: первая строка бесполезна, дублирование кода
        self.carrier.carry_commercial(self.objects)
        return f'{self.carrier.carry_commercial(self.objects)}'

    # КОММЕНТАРИЙ: тоже не отличается реализация
    def add_objects(self, new_objects):
        """Добавляет пассажиров/грузы, перевозка которых осуществляется коммерческим самолетом"""
        self.objects += new_objects


cargo = Cargo()
passenger = Passenger()

commercial_plane = Commercial(cargo, 300)
print(commercial_plane.display_description())
commercial_plane.add_objects(23)
print(commercial_plane.display_description())

commercial_plane = Commercial(passenger, 234)
print(commercial_plane.display_description())
commercial_plane.add_objects(54)
print(commercial_plane.display_description())

military_plane = Military(cargo, 100)
print(military_plane.display_description())
military_plane.add_objects(67)
print(military_plane.display_description())

# stdout:
"""
Коммерческий самолет перевозит 300 товаров
Коммерческий самолет перевозит 323 товаров
Коммерческий самолет перевозит 234 пассажиров
Коммерческий самолет перевозит 288 пассажиров
Военный самолет перевозит 100 боеприпасов
Военный самолет перевозит 167 боеприпасов
"""


# ИТОГ: очень хорошо — 4/6
