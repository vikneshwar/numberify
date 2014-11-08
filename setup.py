import numberify
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()


setup(
    name=numberify.__title__,
    version=numberify.__version__,
    author=numberify.__version__,
    url="https://github.com/darkowlzz/numberify",
    description="Prepend each line of a file with line number",
    long_description=readme,
    packages=find_packages(),
    setup_requires=['nose'],
    test_suite='test'
)