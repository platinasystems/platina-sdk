from setuptools import setup, find_packages
from os.path import abspath, dirname, join

PROJECT_NAME = "platina_sdk"
LICENSE = 'Platina Systems License'
SOURCE_DIR = "platina_sdk"
PROJECT_GIT_URL = "https://github.com/platinasystems/platina-sdk"
AUTHOR_NAME = "mplatina"
AUTHOR_EMAIL = "mplatina@platinasystems.com"
DESCRIPTION = "Python Library"
KEYWORDS = ['platina']
CLASSIFIERS = '''
Programming Language :: Python :: 3
'''.strip().splitlines()

REQUIREMENTS = [
    'distro >= 1.4.0',
    'requests >= 2.21',
    'urllib3 >= 1.24'
    ]

CURRENT_DIR = dirname(abspath(__file__))

with open(join(CURRENT_DIR, SOURCE_DIR, '__init__.py')) as init_py:
    for line in init_py:
        if line.startswith("__version__"):
            VERSION = line.strip().split("=")[1].strip(" '\"")
            break
        else:
            VERSION = "1.0.0"

DOWNLOAD_URL = PROJECT_GIT_URL + "/archive/master.zip"
print("VERSION=%s" % VERSION) 
setup(
    name = PROJECT_NAME,
    packages=[SOURCE_DIR, SOURCE_DIR+".s3", SOURCE_DIR+".pcc"],
    version = VERSION,
    license = LICENSE,
    author = AUTHOR_NAME,
    author_email = AUTHOR_EMAIL,
    description = DESCRIPTION,
    url = PROJECT_GIT_URL,
    download_url = DOWNLOAD_URL,
    keywords = KEYWORDS,
    install_requires = REQUIREMENTS,
    classifiers = CLASSIFIERS
)
