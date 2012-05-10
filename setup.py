from setuptools import setup
import os, shutil

setup(name='OpenKeyval CLI',
      version='1.0',
      description='Command line interface for PyOpenKeyval',
      author='Joseph McCullough',
      author_email='joseph@vertstudios.com',
      packages = ['pyopenkeyval'],
      scripts=['okv']
     )
