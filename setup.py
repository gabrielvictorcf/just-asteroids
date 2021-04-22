from setuptools import setup

longDescription = open('README.md').read()
setup(
    name='just-asteroids',
    version='0.1.0',
    description='Simple terminal clone of Asteroids made on curiosity :)',
    author='Gabriel Victor',
    author_email='gabrielvcf@outlook.com',
    url='https://github.com/gabrielvictorcf/just-asteroids',
    download_url='https://github.com/gabrielvictorcf/just-asteroids',
    long_description=longDescription,
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords='terminal-game asteroids',
    license='MIT',
    packages=['justasteroids'],
    entry_points={'console_scripts': ['just-asteroids=justasteroids.__main__:main']},
    include_package_data=True,
    install_requires=['keyboard'],
    python_requires='>=3',
)