from sys import argv
from os import system

system(f'python -m img_fit {' '.join(argv[1:])}')