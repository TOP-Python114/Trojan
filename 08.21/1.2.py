import itertools

def permutations(set_letter):
    set_permutations = itertools.permutations(set_letter)
    for n in set_permutations:
        yield "".join(n)


set_letter = {'a', 'b', 'c'}
perm = permutations(set_letter)
for n in perm:
    print(n, end=" ")


# stdout:
'''acb abc cab cba bac bca'''
