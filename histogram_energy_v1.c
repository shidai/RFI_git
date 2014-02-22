// calculate the histogram of energy
// input: a is the start point, n is the number of bins; an one column file listing the energy is needed (awk '{print $5}' ../countRFI.txt > energy)
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main (int argc, char *argv[])
{
	int a;
	int n;

	if (argc != 4)
	{
		printf ("Usage: gsl-histogram xmin xmax n\n"
			"Computes a histogram of the data "
			"on stdin using n bins from xmin "
			"to xmax\n");
		exit (0);
	}

	a = atoi (argv[2]);
	//b = atof (argv[3]);
	n = atoi (argv[3]);

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

		while (fscanf (fp, "%f", &x) == 1)
		{
			if ( ((x-a)/10000) < n )
			{
				index = (x - a)/10000;
				count[index] += 1;
			}
		}
		//printf ("%d\n", index);
	
		if (fclose (fp) != 0)
			fprintf (stderr, "Error closing\n");

		for (i = 0; i < n; i++)
		{
			printf ("%d %d\n", a+i*10000, count[i]);
			printf ("%d %d\n", a+(i+1)*10000, count[i]);
		}

	}

	return 0;
}

