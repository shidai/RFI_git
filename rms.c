// read binary file
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main (int argc, char *argv[])
//int readbinary ( char *filename, int *ntxt, double *x, double *y )
{
	// read data 
    FILE *fp;
	if ((fp = fopen(argv[1], "r")) == NULL)
	{
		fprintf (stdout, "Can't open file\n");
		exit(1);
	}

	float x;
    int i;

	// printf ("%d\n", i);
	float rms;

	rms=0.0;
	i=0;
	while (fread (&x, sizeof(float), 1, fp) == 1)
		{
			//puts (c);
			//printf ("%s %f %f\n", name[i], x[i], y[i]);
			rms+=x*x;
			i++;
		}
	rms=sqrt(rms/i);
	//printf ("number of point: %d\n", i);

	printf ("%s %f\n", argv[1], rms);

	if (fclose (fp) != 0)	
	    fprintf (stderr, "Error closing\n");
	
	return 0;
}
    	
