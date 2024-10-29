from setuptools import find_packages, setup

setup(
    name='web3ai',
    packages=find_packages(include=['web3ai']),
    version='0.1.0',
    description='A natural language wrapper for blockchain explorer APIs',
    author='shantanu',
    install_requires=[
        'aiohttp==3.10.10',
        'aioresponses==0.7.6',
        'openai==1.52.2', 
    ],
    extras_require={
        'testing': ['pytest'],
    },
)
