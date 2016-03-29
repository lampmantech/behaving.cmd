"""
This package is Python 2 only for the moment.
"""

from setuptools import setup, find_packages

version = '0.0.1.dev2'

dParams = dict(name='behaving_cmd',
               version=version,
               description="Behavior-Driven-Development testing for commands and files",
               long_description=open("README.rst").read() + open("CHANGELOG.txt").read(),
               classifiers=[
                   "Development Status :: 3 - Alpha",
                   "Environment :: Console",
                   "Intended Audience :: Developers",
                   "Topic :: Software Development :: Testing",
                   "Topic :: Software Development :: Libraries",
                   "Topic :: Software Development :: Libraries :: Python Modules"
#                   "Topic :: Utilities",
#                   "Operating System :: Microsoft :: Windows",
                   "Operating System :: POSIX",
                   "Operating System :: POSIX :: AIX",
                   "Operating System :: POSIX :: Linux",
                   "Programming Language :: C++",
                   "Programming Language :: Python",
                   "Programming Language :: Python :: 2",
                   "Programming Language :: Python :: 2.7",
                   ],
               keywords="BDD Behavior-Driven-Development testing",
               author='Lampman Tech',
               url='http://github.com/lampmantech/behaving_cmd',
               license='GPL',
               packages=find_packages('src', exclude=['tests']),
               package_dir={'': 'src'},
               namespace_packages=['behaving'],
               include_package_data=True,
               zip_safe=False,
               # we plan to make sh and cmd2 soft dependencies later
               # for now, there are some steps that require sh/pbs
               install_requires=['setuptools', 'behaving'],
               # The code is being developed Unix-only for now - 'Windows', 
               platforms = ['Linux', 'Unix', 'MacOS X'],
           )

if __name__ == '__main__':
    setup(**dParams)
