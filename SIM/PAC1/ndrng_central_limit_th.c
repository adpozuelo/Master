/*
  Simulación <PAC1>
  Antonio Díaz Pozuelo <adpozuelo@uoc.edu>
  Normal ditribution random number generator
  Central limit theorem method
 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
  srand((unsigned)time(NULL));
  double a=0;
  for (int i=0;i<12;i++) {
    a+=((double)rand()/(double)RAND_MAX);
  }
  a-=6;
  printf("%f\n",a);
  return 0;
}
