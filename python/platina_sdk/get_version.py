from setuptools import setup, find_namespace_packages
from os.path import abspath, dirname, join

CURRENT_DIR = dirname(abspath(__file__))
with open(join(CURRENT_DIR, '__init__.py')) as init_py:
    for line in init_py:
        if line.startswith("__version__"):
            VERSION = line.strip().split("=")[1].strip(" '\"")
            break
        else:
            VERSION = "1.0.0"
print(VERSION)
