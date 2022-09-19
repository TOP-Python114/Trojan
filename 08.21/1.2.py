import itertools
set_letter = {'a', 'b', 'c'}

def permutations(set_letter):
    set_permutations = itertools.permutations(set_letter)
    for n in set_permutations:
        yield "".join(n)

perm = permutations(set_letter)
for n in perm:
    print(n, end=" ")

'''acb abc cab cba bac bca'''


