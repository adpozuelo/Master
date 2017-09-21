#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

int main (int argc, char *argv[]) {
  struct timeval start_time, end_time, wall_time;
  gettimeofday(&start_time, NULL);
  int    N; //size of columns and rows (matrices)
  int	 tid, nthreads, i, j, k;
  double **a, **b, **c;
  double *a_block, *b_block, *c_block;
  double **res;
  double *res_block;

  if(argc<2){
    printf("Usage: mm matrix_size\n");
    exit(-1);
  }

  N = atoi(argv[1]);

  a = (double **) malloc(N*sizeof(double *)); /* matrix a to be multiplied */
  b = (double **) malloc(N*sizeof(double *)); /* matrix b to be multiplied */
  c = (double **) malloc(N*sizeof(double *)); /* result matrix c */

  a_block = (double *) malloc(N*N*sizeof(double)); /* Storage for matrices */
  b_block = (double *) malloc(N*N*sizeof(double));
  c_block = (double *) malloc(N*N*sizeof(double));

  /* Result matrix for the sequential algorithm */
  res = (double **) malloc(N*sizeof(double *));
  res_block = (double *) malloc(N*N*sizeof(double));

  for (i=0; i<N; i++)   /* Initialize pointers to a */
    a[i] = a_block+i*N;

  for (i=0; i<N; i++)   /* Initialize pointers to b */
    b[i] = b_block+i*N;
  
  for (i=0; i<N; i++)   /* Initialize pointers to c */
    c[i] = c_block+i*N;

  for (i=0; i<N; i++)   /* Initialize pointers to res */
    res[i] = res_block+i*N;

  for (i=0; i<N; i++) /* last matrix has been initialized */
    for (j=0; j<N; j++)
      a[i][j]= (i+j) * ((double) rand());
  for (i=0; i<N; i++)
    for (j=0; j<N; j++)
      b[i][j]= i * j * ((double) rand());
  for (i=0; i<N; i++)
    for (j=0; j<N; j++)
      c[i][j]= 0.0;

  for (i=0; i<N; i++) {
    for(j=0; j<N; j++) {    
      for (k=0; k<N; k++) {
        c[i][j] += a[i][k] * b[k][j];
      }
    }
  }

  gettimeofday(&end_time, NULL);
  timersub(&end_time, &start_time, &wall_time);
  printf("%ld.%08ld\n",(long int)wall_time.tv_sec, (long int)wall_time.tv_usec);
  exit(0);
}
