from setuptools import setup, find_packages
import os

version = '1.0'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.rst')
    + '\n' +
    read('js', 'blocksit', 'test_blocksit.rst')
    + '\n' +
    read('CHANGES.rst'))

setup(
    name='js.blocksit',
    version=version,
    description="fanstatic blocksit jQuery.",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Lugensa GmbH',
    author_email='jd@lugensa.com',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'setuptools',
        'js.jquery',
    ],
    entry_points={
        'fanstatic.libraries': [
            'js.blocksit = js.blocksit:library',
        ],
    },
)
