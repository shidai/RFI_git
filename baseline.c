// read binary file
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int read (int *n, char *filename)
//int readbinary ( char *filename, int *ntxt, double *x, double *y )
{
    FILE *fp;
	int i;
	if ((fp = fopen(filename, "r")) == NULL)
	{
		fprintf (stdout, "Can't open file\n");
		exit(1);
	}

	i = 0;
	float x;

	while (fread (&x, sizeof(float), 1, fp) == 1)
		{
			//printf ("%f\n", x);
			//puts (c);
			//printf ("%s %f %f\n", name[i], x[i], y[i]);
			i++;
		}
	(*n)=i;
	//printf ("number of point: %d\n", i);

	if (fclose (fp) != 0)	
	    fprintf (stderr, "Error closing\n");
	
	return 0;
}
    	
int main (int argc, char *argv[])
{
        /*
        // calculate the time of the file
	float hour, minute, second, time;
	hour=atof(argv[2]);
	minute=atof(argv[3]);
	second=atof(argv[4]);
        	
        time=hour*60*60+minute*60+second;
	*/

        ////////////////////////////////////////////////////////
	int num;

	// get the number of points
	read(&num,argv[1]);

	// arrange a space to store the data
	//float *data;
	//data=(float *)malloc(sizeof(float)*num);
	
	// read data 
    FILE *fp;
	if ((fp = fopen(argv[1], "r")) == NULL)
	{
		fprintf (stdout, "Can't open file\n");
		exit(1);
	}

	//int i;
	float x;

	// printf ("%d\n", i);
	float ave;

	ave=0.0;
	//i=0;
	while (fread (&x, sizeof(float), 1, fp) == 1)
		{
			//data[i]=x;
			//puts (c);
			//printf ("%s %f %f\n", name[i], x[i], y[i]);
			ave+=x;
			//i++;
		}
	ave=ave/num;
	printf ("%lf\n", ave);
	//printf ("%lf %lf\n", time,ave);

	//free(data);
	if (fclose (fp) != 0)	
	    fprintf (stderr, "Error closing\n");
	
	return 0;
}
    	
