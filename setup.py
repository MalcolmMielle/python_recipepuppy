import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "recipepuppy",
    version = "0.0.1",
    author = "Malcolm Mielle",
    author_email = "malcolm.mielle@gmail.com",
    description = ("A wrapper for the API of Recipe Puppy"),
    license = "Beerware",
    keywords = "recipe ingredient puppy",
    url = "https://github.com/MalcolmMielle/python_recipepuppy",
    packages=['.'],
    long_description=read('README.md'),
    platforms=['any'],
    classifiers=[
        "Development Status :: 1 - Beta",
        "Topic :: Internet :: WWW/HTTP :: Recipe",
    ],
)