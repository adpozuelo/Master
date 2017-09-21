#!/usr/bin/python
import sys
import os
import time

mSize=['10', '50', '100', '200']
threads=['2','3','4']
schedule=['static','dynamic','guided']
jobs=100
job=0
while job < jobs:
    for m in mSize:
        command="qsub mm_serial.sge "+m+" mm_serial_"+m+".out"
        os.system(command)
        time.sleep(1)
        for t in threads:
            for s in schedule:
                command="qsub -pe openmp "+t+" mm_omp.sge "+m+" "+t+" "+s+" mm_omp_"+m+"_"+t+"_"+s+".out"
                os.system(command)
                time.sleep(5)
    job+=1
