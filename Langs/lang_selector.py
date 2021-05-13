import random

from properties import LANGS

r = random.randint(0, len(LANGS)-1)
print('Selected languages:', LANGS[r])
