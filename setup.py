from setuptools import setup

setup(
    name='fix-author',
    version='1.0',
    packages=['fix_author'],
    install_requires=['rbnf', 'wisepy'],
    license='MIT',
    author='thautwarm',
    keywords='git commit, fix author',
    description='fix author info in git commits',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    python_requires='>=3.6.0',
    url='https://github.com/thautwarm/fix-author',
    author_email='twshere@outlook.com',
    platforms='any',
    entry_points={'console_scripts': ['fix-author=fix_author.cli:main']},
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
    zip_safe=False)
