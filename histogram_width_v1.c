#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main (int argc, char *argv[])
{
	double a;
	int n;

	if (argc != 4)
	{
		printf ("Usage: gsl-histogram xmin xmax n\n"
			"Computes a histogram of the data "
			"on stdin using n bins from xmin "
			"to xmax\n");
		exit (0);
	}

	a = atof (argv[2]);
	//b = atof (argv[3]);
	n = atoi (argv[3]);

	int *count = (int *)malloc(n * sizeof(int));

	int i;
	for (i = 0; i < n; i++)
	{
		count[i] = 0;
	}

	{
		int x;
		int index;

		FILE *fp;
		if ((fp = fopen(argv[1], "r")) == NULL)
		{
			fprintf (stdout, "Can't open file\n");
			exit(1);
		}

		while (fscanf (fp, "%d", &x) == 1)
		{
			if ( (x-a) < n )
			{
				index = x - a;
				count[index] += 1;
			}
		}
	
		if (fclose (fp) != 0)
			fprintf (stderr, "Error closing\n");

		for (i = 0; i < n; i++)
		{
			printf ("%d %d\n", i, count[i]);
			printf ("%d %d\n", i+1, count[i]);
		}

	}

	return 0;
}

