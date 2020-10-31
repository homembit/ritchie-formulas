#!/usr/bin/python3
import os

from formula import formula

err = 0

try:
    import cowsay
except ImportError:
    print("Install cowsay with the command: pip3 install cowsay")
    err = err + 1

try:
    import tensorflow
except ImportError:
    print("Install tensorflow with the command: pip3 install tensorflow")
    err = err + 1

if (err > 0):
    print ("Please install the missing dependencies with the commands informed and run this formula again.")
else:
    cowsay.cow("You are good to go!")
