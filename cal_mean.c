// calculate the average, sigma and rms of each beam
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main (int argc, char *argv[])
{
	// get the number of data points
	int npoints;

	npoints=atoi(argv[2]);

	////////////////////////////////////////////////////////
	int num;

	num=npoints;

	// arrange a space to store the data
	float *data;
	data=(float *)malloc(sizeof(float)*num);
	
	// read data 
    FILE *fp;
	if ((fp = fopen(argv[1], "r")) == NULL)
	{
		fprintf (stdout, "Can't open file\n");
		exit(1);
	}

	int i;
	float x;

	// printf ("%d\n", i);
	float ave;

	ave=0.0;
	i=0;
	while (fread (&x, sizeof(float), 1, fp) == 1)
		{
			data[i]=x;
			//puts (c);
			//printf ("%s %f %f\n", name[i], x[i], y[i]);
			ave+=x;
			i++;
		}
	ave=ave/num;

	printf ("%d\n", (int)(ave)); 
	
	free(data);

	if (fclose (fp) != 0)	
	    fprintf (stderr, "Error closing\n");
	
	return 0;
}
    	
