#include "mpi.h"
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <omp.h>

void matmul(int my_size){
	int	i, j, k;
	double **a, **b, **c;
	double *a_block, *b_block, *c_block;
	int NRA, NCA, NCB;

	NRA = my_size; NCA = my_size; NCB = my_size;

	a = (double **) malloc(NRA*sizeof(double *)); /* matrix a to be multiplied */
	b = (double **) malloc(NCA*sizeof(double *)); /* matrix b to be multiplied */
	c = (double **) malloc(NRA*sizeof(double *)); /* result matrix c */

	a_block = (double *) malloc(NRA*NCA*sizeof(double)); /* Storage for matrices */
	b_block = (double *) malloc(NCA*NCB*sizeof(double));
	c_block = (double *) malloc(NRA*NCB*sizeof(double));

	for (i=0; i<NRA; i++)   /* Initialize pointers to a */
		a[i] = a_block+i*NRA;

	for (i=0; i<NCA; i++)   /* Initialize pointers to b */
		b[i] = b_block+i*NCA;
  
	for (i=0; i<NRA; i++)   /* Initialize pointers to c */
		c[i] = c_block+i*NRA;

    for (i=0; i<NRA; i++) /* last matrix has been initialized */
		for (j=0; j<NCA; j++)
			a[i][j]= (double) (i+j);
    for (i=0; i<NCA; i++)
		for (j=0; j<NCB; j++)
			b[i][j]= (double) (i*j);
    for (i=0; i<NRA; i++)
		for (j=0; j<NCB; j++)
			c[i][j]= 0.0;
	
#pragma omp parallel for shared(a,b,c) private(i,j,k) schedule(static)
    for (i=0; i<NRA; i++) {
		for(j=0; j<NCB; j++) {    
			for (k=0; k<NCA; k++) {
				c[i][j] += a[i][k] * b[k][j];
			}
		}
    }

}

int main (int argc, char *argv[]) {
	struct timeval start_time, end_time, wall_time;
	gettimeofday(&start_time, NULL);

	int SIZE=atoi(argv[1]);
	int ITERS=atoi(argv[2]);
	int IMBALANCE=atoi(argv[3]); // 0 is not imbalance
	int IMBALANCE_BASE=atoi(argv[4]);

	int MyProc, tag=1, i, j;
	MPI_Status *status;

	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &MyProc);


	for(i=0; i<ITERS; i++){
		for(j=0; j<IMBALANCE_BASE+IMBALANCE*MyProc; j++){
			matmul(SIZE);
		}
		MPI_Barrier(MPI_COMM_WORLD);
		/*if(MyProc == 0){
			printf("Iteration %d done!\n", i);
			}*/
	}

	MPI_Finalize();

	if(MyProc == 0){
		gettimeofday(&end_time, NULL);
		timersub(&end_time, &start_time, &wall_time);
		printf("%ld.%08ld\n",(long int)wall_time.tv_sec, (long int)wall_time.tv_usec);
	}	
  	exit(0);
}

