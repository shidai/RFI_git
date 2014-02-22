#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main (int argc, char *argv[])
{
	int n;

	if (argc != 3)
	{
		printf ("Usage: gsl-histogram xmin xmax n\n"
			"Computes a histogram of the data "
			"on stdin using n bins from xmin "
			"to xmax\n");
		exit (0);
	}

	//b = atof (argv[3]);
	n = atoi (argv[2]);

	int *count = (int *)malloc(n * sizeof(int));

	int i;
	for (i = 0; i < n; i++)
	{
		count[i] = 0;
	}

	{
		float x;
		int index;

		FILE *fp;
		if ((fp = fopen(argv[1], "r")) == NULL)
		{
			fprintf (stdout, "Can't open file\n");
			exit(1);
		}

		double cut = log10(30000);
		while (fscanf (fp, "%f", &x) == 1)
		{
			if ( log10(x)-cut > 0 && ((log10(x)-cut)/0.02) < n )
			{
				index = (int)((log10(x)-cut)/0.02);
				count[index] += 1;
			}
		}
		//printf ("%d\n", index);
	
		if (fclose (fp) != 0)
			fprintf (stderr, "Error closing\n");

		for (i = 0; i < n; i++)
		{
			printf ("%f %d\n", i*0.02+cut, count[i]);
			printf ("%f %d\n", (i+1)*0.02+cut, count[i]);
		}

	}

	return 0;
}

