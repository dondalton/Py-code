#cd .\documents\python
#run: python setup.py py2exe
#results in the .\dist directory

from distutils.core import setup
import py2exe

setup(console=['CDMAnbrlistBSC2.py'])
