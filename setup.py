from setuptools import setup, find_packages

setup(name='nd_to_json',
  version='0.0.0',
  install_requires = [
    "numpy",
    "orjson"
  ],
  packages=find_packages())
