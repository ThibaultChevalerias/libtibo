from setuptools import setup

setup(
    name='libtibo',
    version='0.1.0',
    description='Personal test package',
    url='https://github.com/ThibaultChevalerias/libtibo',
    author='Thibault Chevalerias',
    author_email='',
    license='GPLv3',
    packages=['libtibo'],
    install_requires=['numpy',
                      'pandas'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
)
