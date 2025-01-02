from setuptools import setup, find_packages

setup(
    name='pytestreport-md',
    version='0.1.5',
    packages=find_packages(),
    install_requires=[
        'pytest',
        'pytest-cov',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'pytestreport = pytestreport.cli:cli',
        ],
    },
)
