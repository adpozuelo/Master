#!/usr/bin/python
import sys
import os
import time

s=['A', 'B', 'C']
t=['2','4']
jobs=10
job=0
while job < jobs:
    for si in s:
        for ti in t:
            command="qsub -pe openmp "+ti+" npb_omp_cg.sge "+ti+" "+si+" npb_omp_cg_"+ti+"_"+si+".out"
            os.system(command)
            time.sleep(5)
    job+=1
