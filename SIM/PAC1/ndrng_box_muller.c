/*
  Simulación <PAC1>
  Antonio Díaz Pozuelo <adpozuelo@uoc.edu>
  Normal ditribution random number generator
  Box Muller method
  Mean = 0, Standard desviation = 1
 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int main() {
  double mu=0;
  double sigma=1;
  srand((unsigned)time(NULL));
  double u1=((double)rand()/(double)RAND_MAX);
  double u2=((double)rand()/(double)RAND_MAX);
  double z0=sqrt(-2.0*log(u1))*cos(2 * M_PI * u2);
  double z1=sqrt(-2.0*log(u1))*sin(2 * M_PI * u2);

  printf("%f %f\n",z0*sigma+mu,z1*sigma+mu);
  return 0;
}
