import itertools

# ИСПРАВИТЬ: имя параметра set_letter — не было ограничения на то, что функция может принимать множество, содержащие только строки — в множестве могут быть различные объекты
# ДОБАВИТЬ: аннотации типов параметров и возвращаемого значения, документацию для функции
def permutations(set_letter):
    # ИСПРАВИТЬ: объект, возвращаемый функцией itertools.permutations() используется только один раз — переменная избыточна
    set_permutations = itertools.permutations(set_letter)
    for n in set_permutations:
        # ИСПРАВИТЬ: а если в множестве присутствуют не только объекты str?
        yield "".join(n)


set_letter = {'a', 'b', 'c'}
perm = permutations(set_letter)
for n in perm:
    print(n, end=" ")
print()

set_mix = {'a', 2, 'c'}
print(*permutations(set_mix))


# stdout:
# acb abc cab cba bac bca
# TypeError: sequence item 1: expected str instance, int found


# ИТОГ: внимательнее с типами объектов — 4/6
