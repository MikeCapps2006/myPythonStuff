from collections import Counter
from collections import namedtuple

my_list = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3]
counter = Counter(my_list)
print(counter)

print(counter.values())

Dog = namedtuple('Dog', ['age', 'breed', 'name'])

oakley = Dog(5, 'Mut', 'Oakley')

print(oakley.name)