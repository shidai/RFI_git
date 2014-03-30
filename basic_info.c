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

	// get the beam number
	int beam;

	beam=atoi(argv[3]);

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
	float ave,rms;

	ave=0.0;
	rms=0.0;
	i=0;
	while (fread (&x, sizeof(float), 1, fp) == 1)
		{
			data[i]=x;
			//puts (c);
			//printf ("%s %f %f\n", name[i], x[i], y[i]);
			ave+=x;
			rms+=x*x;
			i++;
		}
	ave=ave/num;
	rms=sqrt(rms/num);

	float devi;
	devi=0.0;
	for (i=0;i<num;i++)
	{
		devi+=(data[i]-ave)*(data[i]-ave);
	}
	devi=sqrt(devi/num);

	printf ("%d %s %f\n", beam, argv[1], rms); // argv[3] is the beam number
	
	free(data);

	if (fclose (fp) != 0)	
	    fprintf (stderr, "Error closing\n");
	
	return 0;
}
    	
