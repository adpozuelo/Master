#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <sys/time.h>

int main(int argc, char *argv[]){
	struct timeval start_time, end_time, wall_time;
	gettimeofday(&start_time, NULL);
	int N = atoi(argv[1]);
	int a[N], i;
	for (i=0; i<N; i++)
		a[i]=1;
	int sum=0;
	#pragma omp parallel for reduction(+:sum)
    for(i=0; i<N; i++)
        sum += a[i];
	//printf("Suma = %d\n", sum);
	gettimeofday(&end_time, NULL);
	timersub(&end_time, &start_time, &wall_time);
	printf("%ld.%08ld\n",(long int)wall_time.tv_sec, (long int)wall_time.tv_usec);
	return 0;
}
