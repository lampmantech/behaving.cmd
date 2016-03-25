from setuptools import setup, find_packages

version = '0.0.1-dev0'

setup(name='behaving_cmd',
      version=version,
      description="Behavior-Driven-Development testing for commands and files",
      long_description=open("README.rst").read() + open("CHANGES.txt").read(),
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
      ],
      keywords='BDD Behavior-Driven-Development testing',
      author='Lampman Tech',
      url='http://github.com/lampmantech/behaving_cmd',
      license='GPL',
      packages=find_packages('src', exclude=['tests']),
      package_dir={'': 'src'},
      namespace_packages=['behaving'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools', 'parse', 'behave', 'sh'],
      )
