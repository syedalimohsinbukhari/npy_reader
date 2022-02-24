import pathlib

from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent
INSTALL_REQUIRES = (HERE / 'requirements.txt').read_text().splitlines()

setup(
        name='npy_reader',
        version='1.0.1',
        packages=find_packages(where="src"),
        url='https://github.com/AstrophysicsAndPython/npy_reader',
        license='MIT',
        author='Astrophysics and Python, Syed Ali Mohsin Bukhari',
        author_email='astrophysicsandpython@gmail.com, syedali.b@outlook.com',
        description='A simple tool to read and display numpy (.npy) files.',
        python_requires=">=3.7",
        install_requires=INSTALL_REQUIRES
        )
