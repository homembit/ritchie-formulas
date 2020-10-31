#!/usr/bin/python3
import os
import time
import cowsay
from formula import formula

n_epochs = os.environ.get('NUMBER_EPOCHS')
early_stop = os.environ.get('EARLY_STOP')
print("Staring MNIST CNN Trainning with " + n_epochs + " epochs...\n\n\n")
start = time.time()
Acc = (formula.Run(n_epochs,early_stop))
end = time.time()
cowsay.cow(Acc + "\nDuration: " + "{:.2f}".format(end - start) + " s")
