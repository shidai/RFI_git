// calculate the histogram of width
// input: n is the number of bins; an one column file listing the width is needed (awk '{print $4}' ../countRFI.txt > width)
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

	//a = atof (argv[2]);
	//b = atof (argv[3]);
	n = atoi (argv[2]);

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
			if ( log10(x) < n*0.2 )
			{
				index = ceil((log10(x)/0.2));
				//index = (int)(log10(x)/0.2);
				count[index] += 1;
			}
		    //	index = x - a;
		    //	count[index] += 1;
		}
	
		if (fclose (fp) != 0)
			fprintf (stderr, "Error closing\n");

		for (i = 0; i < n; i++)
		{
			printf ("%f %d\n", i*0.2, count[i]);
			printf ("%f %d\n", (i+1)*0.2, count[i]);
		}

	}

	return 0;
}

