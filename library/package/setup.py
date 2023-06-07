from setuptools import setup

setup(
    name='name_module',
    version='1.0.0',
    description='description tool',
    author='name_author',
    author_email='author@e-mail.com',
    url='https://github.com/...',
    packages=['name_module']
    install_requires=['selenium', 'pandas']
    classifiers=[
        'Development Status :: 3 - Alpha',
		'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Information Analysis'
    ]
)