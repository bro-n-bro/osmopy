from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='osmopy',
    version='0.0.2',
    packages=['osmopy', 'osmopy.interfaces'],
    url='https://github.com/bro-n-bro/osmopy',
    license='MIT',
    author='bro-n-bro-0',
    author_email='',
    description='Tools for Osmosis wallet management, offline transaction signing and broadcasting',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'ecdsa',
        'bech32',
        'hdwallets',
        'mnemonic',
        'typing-extensions',
        'requests'
      ],
    zip_safe=False,
)
