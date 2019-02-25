from setuptools import setup, find_packages


with open('README.md') as fp:
    long_description = fp.read()

CLASSIFIERS = """
Development Status :: 3 - Alpha
Intended Audience :: Science/Research
Intended Audience :: Developers
Programming Language :: Python :: 3.6
Topic :: Software Development
Topic :: Scientific/Engineering
"""

setup(
    name='phytools',
    version='0.1.0',
    author='',
    author_email='euphiment@gmx.de',
    url='https://github.com/kricki/phytools',
    description='Tools for physicists',
    long_description=long_description,
    packages=find_packages(),
    classifiers=[f for f in CLASSIFIERS.split('\n') if f],
    install_requires=['numpy', 'scipy'],
)
