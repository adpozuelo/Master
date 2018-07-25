/*
  MonteCarlo (SIS) - RC - UOC - URV - PEC4
  adpozuelo@uoc.edu
  Compile: gcc -I/usr/local/include/igraph -L/usr/local/lib -ligraph -Ofast mc.cpp -o mc
  Run: ./mc
*/

#include <stdio.h>
#include <igraph.h>
#include <random>

#define N 500 // <-- Change numer of nodes
#define NDELTA 51
#define TMAX 1000
#define TTRANS 900
#define TSTUDY TMAX - TTRANS
#define ITERS 100

int main() {

	std::default_random_engine generator;
	std::uniform_real_distribution<float> distribution(0.0,1.0);
	
	igraph_t g;
	igraph_vector_t v;
	igraph_vector_init(&v, 8);
	int m = 4; // barabasi m <<-- Change edges generated for each vertex
	//float p = 0.1; // ER p <<-- Change probability ER(N,p)

	igraph_barabasi_game(&g, N, /*power=*/ 1, m, 0, 0, /*A=*/ 1, 0, IGRAPH_BARABASI_PSUMTREE, /*start_from=*/ 0); // <-- Barabási-Albert graph
	//igraph_erdos_renyi_game(&g, IGRAPH_ERDOS_RENYI_GNP, N, p, IGRAPH_UNDIRECTED, IGRAPH_NO_LOOPS); // <-- ER graph

	const char *filenameNet = "./ba_N500_m4.net"; // <-- Change net file name
	//const char *filenameNet = "./er_N500_p01.net"; // <-- Change net file name
	FILE *fp;
	fp = fopen(filenameNet, "w");
	igraph_write_graph_pajek(&g, fp);
	fclose(fp);

	float mu = 0.1; // <-- Change mu
	float rho_0 = 0.1; // <-- initial rho (initial % of infected)
	float rho_iters[ITERS] = {0};
	float rho_tstudy[TSTUDY] = {0};
	float rho[NDELTA] = {0};

	const char *filenameRho = "./ba_N500_m4_mu01_rho01.txt"; // <-- Change output file name
	//const char *filenameRho = "./er_N500_p01_mu01_rho01.txt"; // <-- Change output file name
	fp = fopen(filenameRho, "w");

	for (int beta_delta = 0; beta_delta < NDELTA; ++beta_delta) {
		float beta = beta_delta / (float) (NDELTA - 1);

		for (int iter = 0; iter < ITERS; ++iter) {
			int graphstatus_t0[N] = {0};
			int graphstatus_t1[N] = {0};

			// initial nodes infected
			for (int n = 0; n < N; ++n) {
				if (distribution(generator) < rho_0) {
					graphstatus_t0[n] = 1;
				}
			}

			for (int n = 0; n < N; ++n) {
				graphstatus_t1[n] = graphstatus_t0[n];
			}
			
			for (int time = 0; time < TMAX ; ++time) {
				for (int n = 0; n < N; ++n) {

					if (graphstatus_t0[n] == 1) { // if node is infected, probability of being cured
						if (distribution(generator) < mu) {
							graphstatus_t1[n] = 0;
						}
					} else { // if node is not infected
						igraph_neighbors(&g, &v, n, IGRAPH_ALL); // get its neighbors
						for (int i = 0; i < igraph_vector_size(&v); ++i) {
							if (graphstatus_t0[(long int) VECTOR(v)[i]] == 1) { // if neighbor is infected
								if (distribution(generator) < beta) { // probability to being infected
									graphstatus_t1[n] = 1;
									break;
								}
							}
						}
					}
				}
				
				for (int n = 0; n < N; ++n) {
					graphstatus_t0[n] = graphstatus_t1[n];
				}

				if (time >= TTRANS) { // stats for stationary phase
				 	float reduce_avg = 0.0;
				 	for (int n = 0; n < N; ++n) {
				 		reduce_avg += graphstatus_t0[n];
				 	}
				 	reduce_avg /= N;
				 	rho_tstudy[time - TTRANS] = reduce_avg;
				}

			}
			
			float rho_tstudy_avg = 0.0; // stats for every iteration
			for (int i = 0; i < TSTUDY; ++i) {
				rho_tstudy_avg += rho_tstudy[i];
			}
			rho_tstudy_avg /= TSTUDY;
			rho_iters[iter] = rho_tstudy_avg;
		}
		
		float rho_iter_avg = 0.0; // stats for every delta of beta
		for (int i = 0; i < ITERS; ++i) {
			rho_iter_avg += rho_iters[i];
		}
		rho_iter_avg /= ITERS;
		rho[beta_delta] = rho_iter_avg;
		fprintf(fp, "%f %f\n", beta, rho[beta_delta]);
	}
	
	fclose(fp);
	igraph_destroy(&g);
	return 0;
}
