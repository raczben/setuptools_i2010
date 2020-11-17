from setuptools import setup

setup(
    setup_requires=['pbr'],
    pbr=True,
    name='snek',
    entry_points={
        'console_scripts': [
            'snek = snek:main',
        ],
    }
)