from distutils.core import setup

setup(
    name='twitterbot',
    version='0.1.0',
    author='thricedotted',
    author_email='thricedotted@gmail.com',
    packages=['twitterbot'],
    #scripts=['bin/stowe-towels.py','bin/wash-towels.py'],
    #url='http://pypi.python.org/pypi/TowelStuff/',
    #license='LICENSE.txt',
    description='A simple Python framework for creating Twitter bots.',
    #long_description=open('README.txt').read(),
    install_requires=[
        "tweepy >= 2.3"
    ],
)
