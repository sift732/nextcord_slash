from setuptools import setup

setup(
    name='nextcord_slash',
    version='0.1',
    description='A package for creating and handling Discord slash commands with the nextcord library',
    author='Your Name',
    author_email='your.email@example.com',
    packages=['nextcord_slash'],
    install_requires=[
        'nextcord',
        'discord-py-slash-command'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
