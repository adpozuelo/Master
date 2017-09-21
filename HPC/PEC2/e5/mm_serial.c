#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

int main (int argc, char *argv[]) {
	struct timeval start_time, end_time, wall_time;
	gettimeofday(&start_time, NULL);	
	int    N; //size of columns and rows (matrices)
	int	 tid, nthreads, i, j, k, l;
	double **a, **b, **c, **d, Z;
	double *a_block, *b_block, *c_block, *d_block;

	if(argc<2){
		printf("Usage: mm matrix_size\n");
		exit(-1);
	}

	N = atoi(argv[1]);

	a = (double **) malloc(N*sizeof(double *)); /* matrix a to be multiplied */
	b = (double **) malloc(N*sizeof(double *)); /* matrix b to be multiplied */
	c = (double **) malloc(N*sizeof(double *)); /* result matrix c */
	d = (double **) malloc(N*sizeof(double *)); /* result matrix d */

	a_block = (double *) malloc(N*N*sizeof(double)); /* Storage for matrices */
	b_block = (double *) malloc(N*N*sizeof(double));
	c_block = (double *) malloc(N*N*sizeof(double));
	d_block = (double *) malloc(N*N*sizeof(double));

	for (i=0; i<N; i++)   /* Initialize pointers to a */
		a[i] = a_block+i*N;

	for (i=0; i<N; i++)   /* Initialize pointers to b */
		b[i] = b_block+i*N;
  
	for (i=0; i<N; i++)   /* Initialize pointers to c */
		c[i] = c_block+i*N;

	for (i=0; i<N; i++)   /* Initialize pointers to d */
		d[i] = d_block+i*N;

	for (i=0; i<N; i++) /* last matrix has been initialized */
		for (j=0; j<N; j++)
			a[i][j]= (i+j) * ((double) rand());
	//a[i][j]= i + j;
	for (i=0; i<N; i++)
		for (j=0; j<N; j++)
			b[i][j]= i * j * ((double) rand());
	//b[i][j]= i * j;
	for (i=0; i<N; i++){
		for (j=0; j<N; j++){
			c[i][j]= 0.0;
			d[i][j]= 0.0;
		}
	}

	/* STEP 1: Z is the (integer) sum of ell elements of a anb b */

	Z=0.0;
	for (i=0; i<N; i++) /* last matrix has been initialized */
		for (j=0; j<N; j++){
			Z += a[i][j]+b[i][j]; //Optimization, only one sentence
		}

	//printf("Value of Z: %e\n", Z);

	/* STEP 2: variation of matrix multiplication */

	for (i=0; i<N; i++) {
		for(j=0; j<N; j++) {    
			for (k=0; k<N; k++) {
				c[i][j] += a[i][k] * b[k][j];
				for(l=0; l<i+N+N; l++) {
					if ((l+k)>0)
						c[i][j] -= ((Z*k)+l-k)/(l+k);
				}
			}
		}
	}
	// Debug info
	/*
	  double C=0.0;
	  for (i=0; i<N; i++) {
	  for(j=0; j<N; j++) {    
	  C+=c[i][j];
	  }
	  } 
	  printf("Value of C: %e\n", C);
	*/
	/* STEP 3: add elements of matrices d=a+b */

	for (i=0; i<N; i++) {
		for(j=0; j<N; j++) {
			d[i][j] = a[i][j] + b[i][j];
		}
	}
	// Debug info
	/*
	  double D=0.0;
	  for (i=0; i<N; i++) {
	  for(j=0; j<N; j++) {    
	  D+=d[i][j];
	  }
	  } 
	  printf("Value of D: %e\n", D);
	*/
	gettimeofday(&end_time, NULL);
	timersub(&end_time, &start_time, &wall_time);
	printf("%ld.%08ld\n",(long int)wall_time.tv_sec, (long int)wall_time.tv_usec);
	exit(0);
}

