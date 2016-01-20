from setuptools import setup, find_packages

setup(
    name = 'nsgaiii',
    version = '0.1.0',
    author = 'Luis Martí',
    author_email = 'lmarti@ic.uff.bf',
    description = ('An implementation of the NSGA-III algorithm in Python'),
    license = 'LGNU',
    keywords = ['evolutionary algorithms','genetic algorithms','ga','nsga','moea', 'multi-objective optimization','emoa', 'emo', 'nsga-iii'],
    url = 'http://lmarti.github.io/nsgaiii/',
    packages = find_packages(),
    classifiers = [
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    include_package_data = False,
    install_requires = [
      'numpy','deap'
    ],
    tests_require = [],
    extras_require = {
        'docs': [
          'Sphinx',
          'numpydoc',
        ],
        'tests': [],
    },
)
