#!/usr/bin/python
import sys
import os
import time

mSize=['10', '50', '100']
iters=['10','20','30']
imbalance=['0','10','20']
imbalance_base=['50','60','70']
mpijobs=['8','12','16']
jobs=5
job=0
while job < jobs:
    for m in mSize:
        for i in iters:
            for im in imbalance:
                for imb in imbalance_base:
                    for mpij in mpijobs: 
                        command="qsub -pe orte "+mpij+" -sync y barr_sync_omp.sge "+mpij+" "+m+" "+i+" "+im+" "+imb+" barr_sync_omp_"+mpij+"_"+m+"_"+i+"_"+im+"_"+imb+".out"
                        os.system(command)
    job+=1
