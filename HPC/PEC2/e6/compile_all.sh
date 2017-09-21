#!/bin/bash
mpicc barr_sync_base.c -o barr_sync_base
mpicc -openmp barr_sync_omp.c -o barr_sync_omp
