from setuptools import setup, find_packages

setup(
    name='nextcord_slash',
    version='0.1',
    description='A package for creating and handling Discord slash commands with the nextcord library',
    author='sift732',
    author_email='kanariaking30@gmail.com',
    packages=find_packages(),
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
