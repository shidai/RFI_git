// read binary file, return the number of data points
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main (int argc, char *argv[])
{
    FILE *fp;
	int i;
	if ((fp = fopen(argv[1], "r")) == NULL)
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

	printf ("%d\n", i);

	if (fclose (fp) != 0)	
	    fprintf (stderr, "Error closing\n");
	
	return 0;
}
    	
