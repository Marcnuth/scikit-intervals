'''
Setup Scikit-intervals
'''

from setuptools import setup, find_packages


setup(
    name='scikit-intervals',
    version='0.1.2',

    description=("handling intervals calculation in python"),

    url="https://github.com/Marcnuth/scikit-intervals",

    # Author details
    author="Marcnuth",
    author_email="marcnuth@foxmail.com",

    license="Apache License 2.0",

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3'

    ],

    # What does your project relate to?
    keywords=("intervals", "scikit", "mathematics"),

    packages=find_packages("."),

    install_requires=[
        "numpy",
        "arrow"
    ],

)
