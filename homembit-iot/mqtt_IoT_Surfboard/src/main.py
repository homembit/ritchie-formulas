#!/usr/bin/python3
import os

from formula import formula

input1 = os.environ.get("H_NAME")
input2 = os.environ.get("H_PORT")
input3 = os.environ.get("TOPIC")
formula.Run(input1, input2, input3)
