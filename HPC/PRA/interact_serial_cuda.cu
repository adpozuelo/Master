/*
 * Antonio Díaz Pozuelo - adpozuelo@uoc.edu
 * HPC_PRA - Energy-Potential N-Body Problem (Lennard Jones Interaction Potential)
 * CUDA vs CPU
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define NTHREAD 64
#define NDIM 3
#define SIDE 100

// CUDA kernel
// Energy per particle
__global__ void enerGPU(double eps4, double sig2, double *r, double *eng,
		int nmol) {
	int i = threadIdx.x + blockIdx.x * blockDim.x;
	if (i < nmol) {
		int imol = i * NDIM;
		// Store particle i positions in register to avoid global memory access
		double xi = r[imol];
		double yi = r[imol + 1];
		double zi = r[imol + 2];
		double energ = 0;
		for (int j = 0; j < i; j++) {
			int jmol = j * NDIM;
			int jx = jmol;
			int jy = jmol + 1;
			int jz = jmol + 2;
			double dist2 = pow(xi - r[jx], 2) + pow(yi - r[jy], 2)
					+ pow(zi - r[jz], 2);
			double di6 = pow(sig2 / dist2, 3);
			double ulj = eps4 * di6 * (di6 - 1.0);
			energ = energ + ulj;
		}
		for (int j = i + 1; j < nmol; j++) {
			int jmol = j * NDIM;
			int jx = jmol;
			int jy = jmol + 1;
			int jz = jmol + 2;
			double dist2 = pow(xi - r[jx], 2) + pow(yi - r[jy], 2)
					+ pow(zi - r[jz], 2);
			double di6 = pow(sig2 / dist2, 3);
			double ulj = eps4 * di6 * (di6 - 1.0);
			energ = energ + ulj;
		}
		eng[i] = energ;
	}
}

// CPU kernel
// Energy of the system
void energia(double *energy, double eps4, double sig2, double *r, int nmol) {
	double energ = 0.0;
	int i, j;
	for (i = 0; i < nmol; i++) {
		int id = i * NDIM;
		double xi = r[id];
		double yi = r[id + 1];
		double zi = r[id + 2];
		for (j = i + 1; j < nmol; j++) {
			int jd = j * NDIM;
			int jx = jd;
			int jy = jd + 1;
			int jz = jd + 2;
			double dist2 = pow(xi - r[jx], 2) + pow(yi - r[jy], 2)
					+ pow(zi - r[jz], 2);
			double di6 = pow(sig2 / dist2, 3);
			double ulj = eps4 * di6 * (di6 - 1.0);
			energ = energ + ulj;
		}
	}
	*energy = energ;
}
int main(int argc, char *argv[]) {
	if (argc < 2) {
		printf("Usage: interact_serial NMOL\n");
		exit(-1);
	}
	int nmol = atoi(argv[1]);
	double *r, *energy;
	double *rdev, *edev;
	double eps = 120.0, sigma = 0.1, eps4, sig2, energ;
	clock_t start0, start_cpu, end;
	float cpu_time_used, totalcpu;
	// declare GPU timing events
	cudaEvent_t start, stop, start_t, stop_t;
	int i, j;
	r = (double*) malloc(nmol * NDIM * sizeof(double));
	energy = (double*) malloc(nmol * sizeof(double));
	start0 = clock();
	eps4 = 4 * eps;
	sig2 = pow(sigma, 2);
	// Initialize particle positions (random)
	for (i = 0; i < nmol; i++) {
		for (j = 0; j < NDIM; j++) {
			r[i * NDIM + j] = SIDE * (double) rand() / (double) (RAND_MAX);
		}
	}
	// time CPU energy calculation
	start_cpu = clock();

	// Call CPU kernel for energy calculation
	energia(&energ, eps4, sig2, r, nmol);

	// time CPU results
	end = clock();
	cpu_time_used = 1000 * ((float) (end - start_cpu)) / CLOCKS_PER_SEC;
	totalcpu = 1000 * ((float) (end - start0)) / CLOCKS_PER_SEC;
	printf("%f ", cpu_time_used);
	printf("%f ", totalcpu);
	//printf(" Energy =%f\n", energ);

	// start GPU timing
	cudaEventCreate(&start);
	cudaEventCreate(&stop);
	cudaEventCreate(&start_t);
	cudaEventCreate(&stop_t);
	cudaEventRecord(start_t, 0);

	// Allocate memory on the GPU and transfer positions
	cudaMalloc((void**) &rdev, NDIM * nmol * sizeof(double));
	cudaMalloc((void**) &edev, nmol * sizeof(double));
	cudaMemcpy(rdev, r, NDIM * nmol * sizeof(double), cudaMemcpyHostToDevice);

	int nblock = nmol / NTHREAD;
	cudaEventRecord(start, 0);

	// Call GPU kernel for energy calculation
	enerGPU<<<nblock, NTHREAD>>>(eps4, sig2, rdev, edev, nmol);

	// time GPU record
	cudaEventRecord(stop, 0);
	cudaEventSynchronize(stop);

	// Recall energy per particle from the GPU
	cudaMemcpy(energy, edev, nmol * sizeof(double), cudaMemcpyDeviceToHost);

	// Compute total energy
	double etot = 0;
	for (i = 0; i < nmol; i++) {
		etot = etot + energy[i];
	}
	etot = etot / 2;

	// total GPU time record
	cudaEventRecord(stop_t, 0);
	cudaEventSynchronize(stop_t);
	float elapsedTime;
	cudaEventElapsedTime(&elapsedTime, start, stop);
	float elapsedTimet;
	cudaEventElapsedTime(&elapsedTimet, start_t, stop_t);

	printf("%f ", elapsedTime);
	printf("%f\n", elapsedTimet);
	//printf(" GPU Energy =%f\n", etot);
}
