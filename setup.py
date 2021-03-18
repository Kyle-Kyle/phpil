import os

try:
    from setuptools import setup
    from setuptools import find_packages
    packages = find_packages()
except ImportError:
    from distutils.core import setup
    packages = [x.strip('./').replace('/','.') for x in os.popen('find -name "__init__.py" | xargs -n1 dirname').read().strip().split('\n')]

setup(
      name='phpil',
      version='0.0',
      python_requires='>=3.6',
      description='generating random php for php interpreter fuzzing',
      author='kylebot',
      packages=['phpil'],
      install_requires=[i.strip() for i in open('requirements.txt').readlines() if 'git' not in i]
)
