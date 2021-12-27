from setuptools import setup, find_packages

setup(name='nd_to_json',
  version='0.1.0',
  install_requires = [
    "numpy",
    "orjson>=3.0"
  ],
  packages=find_packages())
