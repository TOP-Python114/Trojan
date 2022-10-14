from abc import ABC, abstractmethod

"""Абстрактный класс, реализующий описание блюда"""
class Dish(ABC):
    def __init__(self, dish_name: str, specification: str, ingredient_list: str, weight: int, price: float, country: str):
        self.dish_name = dish_name
        self.specification = specification
        self.ingredient_list = ingredient_list
        self.weight = weight
        self.price = price
        self.country = country

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

"""Классы, реализующие описание конкретного блюда"""
class CabbageSoup(Dish):
    def dish(self):
        print('Заказываю Щи')

class Minestrone(Dish):
    def dish(self):
        print('Заказываю Минестроне')

class MisoSoup(Dish):
    def dish(self):
        print('Заказываю Мисо суп')

class Sushi_Tuna(Dish):
    def dish(self):
        print('Заказываю Суши Туна')

class Pepperonate(Dish):
    def dish(self):
        print('Заказываю Пеппероната')

class Meatballs(Dish):
    def dish(self):
        print('Заказываю Тефтели')

class Vinaigrette(Dish):
    def dish(self):
        print('Заказываю Винегрет')

class Aranchini(Dish):
    def dish(self):
        print('Заказываю Аранчини')

class Konji(Dish):
    def dish(self):
        print('Заказываю Конджи')

"""Абстрактный класс, реализующий набор ресторанных блюд"""
class AbstractDishFactory(ABC):
    @abstractmethod
    def serving_first_course(self):
        pass

    @abstractmethod
    def serving_second_course(self):
        pass

    @abstractmethod
    def serving_snack(self):
        pass

"""Класс, реализующий блюда русской кухни"""
class RussianCuisineFactory(AbstractDishFactory):
    def serving_first_course(self):
        return CabbageSoup('Щи',
                           'горячее блюдо на основе квашеной или свежей капусты',
                           'курица, капуста белокочанная, картофель, морковь, лук репчатый',
                           250,
                           160,
                           'русская')

    def serving_second_course(self):
        return Meatballs('Тефтели',
                         'блюдо из мясного фарша с добавлением каких-либо круп в виде шариков',
                         'фарш мясной, рис, лук репчатый, томат-паста, сметана, соль, перец',
                         150,
                         200,
                         'русская'
                         )
    def  serving_snack(self):
        return Vinaigrette('Винегрет',
                            'салат из отварных овощей',
                            'свекла, морковь, картофель, лук, капуста, горошек, огурец, растительное масло, соль',
                            100,
                            90,
                            'русская')

"""Класс, реализующий блюда азиатской кухни"""
class AsianCuisineFactory(AbstractDishFactory):
    def serving_first_course(self):
        return MisoSoup('Мисо суп',
                        'традиционный японский суп, состоящий из бульона даси, в который смешивается размягченная паста мисо',
                        'вакаме сушеные, мисо паста, даши, тофу, зеленый лук',
                        200,
                        180,
                        'азиатская')

    def serving_second_course(self):
        return Sushi_Tuna('Суши Туна',
                        'блюдо традиционной японской кухни, приготовленное из риса с уксусной приправой и различных морепродуктов, а также других ингредиентов',
                        'рис, нори, тунец',
                        40,
                        80,
                        'азиатская')

    def serving_snack(self):
        return Konji('Конджи',
                        'китайский гарнир из риса, по консистенции - что-то между супом и пудингом.',
                        'рис, вода',
                        100,
                        80,
                        'азиатская')

"""Класс, реализующий блюда итальянской кухни"""
class ItalianCuisineFactory(AbstractDishFactory):
    def serving_first_course(self):
        return Minestrone('Минестроне',
                            'суп из овощей, в составе которого также могут быть макаронные изделия или рис',
                            'помидоры, лук репчатый, чеснок, стебель сельдерея, морковь, фасоль, бульон куриный, макароны',
                            200,
                            200,
                            'итальянская')

    def serving_second_course(self):
        return Pepperonate('Пеппероната',
                            'овощное блюдо из сладкого перца, который тушится вместе с луком, чесноком и томатами',
                            'сладкий перец, помидоры, лук, чеснок, базилик, соль',
                            150,
                            180,
                            'итальянская')

    def serving_snack(self):
        return Aranchini('Аранчини',
                        'обжаренные рисовые шарики, фаршированные мясным рагу, моццареллой и зелёным горошком',
                        'рис, сыр, яйцо, соль, перец, панировочные сухари',
                        100,
                        200,
                        'итальянская')

"""Фабрика блюд"""
class FactoryDish:
    def __init__(self, factory: AbstractDishFactory):
        self.fac = factory

    def create_menu(self):
        first = self.fac.serving_first_course()
        second = self.fac.serving_second_course()
        snack = self.fac.serving_snack()
        first.dish()
        second.dish()
        snack.dish()

def create_factory(course_name) -> AbstractDishFactory:
    factory_dict = {
        "russia": RussianCuisineFactory,
        "asia": AsianCuisineFactory,
        "italy": ItalianCuisineFactory
    }
    return factory_dict[course_name]()

if __name__ == '__main__':
    course_name = "russia"
    nc = create_factory(course_name)
    app = FactoryDish(nc)
    app.create_menu()

# stdout:
"""
Заказываю Щи
Заказываю Тефтели
Заказываю Винегрет
"""