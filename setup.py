from setuptools import setup, find_packages

setup(
    name='data_ingestion',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/opeyemiolasunkanmianalyst/data_ingestion',
    author='opeyemi olasunkanmi',
    author_email='opeyemiolasunkanmi19@gmail.com'
)