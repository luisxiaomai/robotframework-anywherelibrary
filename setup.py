try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from os.path import join, dirname
import os

execfile(join(dirname(__file__), 'src', 'AnywhereLibrary', 'version.py'))

setup(  
    name = "robotframework-anywherelibrary",
    version= VERSION,
    package_dir  = {'' : 'src'},
    packages=['AnywhereLibrary', 'AnywhereLibrary.base'],
    author = "luis.lu",
    author_email = "luzhenyuhnr@126.com",
    platforms='any',
    install_requires=['decorator >= 3.3.2','selenium >= 2.32.0','robotframework >= 2.6.0','docutils >= 0.8.1'],
    url = "https://github.com/luisxiaomai/robotframework-anywherelibrary",
    description = "Robotframework test library for cross platform:android,ios,browser",
    include_package_data = True,	
    )     
