import sys
import os.path

#if os.path.isfile("~/.bash_aliases"):
f = open("~/.bash_aliases", "a")
f.write("\nalias strip='python "+os.path.realpath("lineremover.py")+"'")
'''
else:
    f = open("~/.bash_aliases", "w")
    f.write("\nalias strip = 'python ~/lineremover/lineremover.py'")
'''
