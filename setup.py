from setuptools import setup, find_packages

setup(
    name = 'pysnsgaiii',
    version = '0.0.1',
    author = 'Luis Martí',
    author_email = 'lmarti@github.com',
    description = ('An implementation of the NSGA-III algorithm in Python'),
    license = 'BSD',
    keywords = 'nsga moea evolutionary genetic multi-objective optimization emoa emo',
    url = 'http://pynsgaiii.github.com',
    packages = find_packages(),
    package_data={,
    classifiers = [
      'Development Status :: 4 - Beta',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: BSD License',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    include_package_data = False,
    install_requires = [
      'numpy',
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
