from setuptools import find_packages, setup

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
        install_requires="numpy>=1.12.5"
        )
