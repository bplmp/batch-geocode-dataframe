from setuptools import setup, find_packages

setup(
    name='batch-geocode-dataframe',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/bplmp/batch-geocode-dataframe',
    license='',
    author='Bernardo Loureiro',
    author_email='',
    description='Batch geocode dataframe',
    install_requires=[open('requirements.txt').read().strip().split('\n')]
)
