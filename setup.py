# -*- coding: utf-8 -*-
from codecs import open
from setuptools import setup, find_packages


with open('README.rst', encoding='utf-8') as fp:
    long_description = fp.read()

install_requires = [
    'Sphinx>=0.6',
]

setup_requires = [
    'pytest-runner',
]

tests_require = [
    'pytest-pep8',
    'pytest',
    'sphinx-testing',
]


setup(
    name='sphinxcontrib-deckjs',
    version='0.0.1',
    url='https://github.com/attakei/sphinxcontrib-deckjs',
    # download_url='http://pypi.python.org/pypi/sphinxcontrib-deckjs',
    license='BSD',
    author='attakei',
    author_email='attakei@gmail.com',
    description='Sphinx "sphinxcontrib-deckjs" extension',
    long_description=long_description,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Framework :: Sphinx :: Extension',
        'Framework :: Sphinx :: Theme',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    namespace_packages=['sphinxcontrib'],
    entry_points = {
        'sphinx_themes': [
            'path = sphinxcontrib.deckjs:get_path',
        ],
    },
    setup_requires=setup_requires,
    tests_require=tests_require,
)
