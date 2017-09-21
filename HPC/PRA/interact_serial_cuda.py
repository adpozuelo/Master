#!/usr/bin/python
import sys
import os
import time

s=['100', '500', '1000', '5000', '10000','20000']
jobs=10
job=0
while job < jobs:
    for si in s:
        command="qsub interact_serial_cuda.sge "+si+" interact_serial_cuda_"+si+".out"
        os.system(command)
        time.sleep(1)
    job+=1
