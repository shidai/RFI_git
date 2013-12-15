#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <gsl/gsl_histogram.h>

int main (int argc, char *argv[])
{
	double a, b;
	size_t n;

	if (argc != 5)
	{
		printf ("Usage: gsl-histogram xmin xmax n\n"
			"Computes a histogram of the data "
			"on stdin using n bins from xmin "
			"to xmax\n");
		exit (0);
	}

	a = atof (argv[2]);
	b = atof (argv[3]);
	n = atoi (argv[4]);

	{
		int x;
		double y;
		gsl_histogram * h = gsl_histogram_alloc (n);
		gsl_histogram_set_ranges_uniform (h, a, b);

		FILE *fp;
		if ((fp = fopen(argv[1], "r")) == NULL)
		{
			fprintf (stdout, "Can't open file\n");
			exit(1);
		}

		while (fscanf (fp, "%d", &x) == 1)
		{
			//y = log10(x);
			y = x;
			gsl_histogram_increment (h, y);
		}
	
		if (fclose (fp) != 0)
			fprintf (stderr, "Error closing\n");

		gsl_histogram_fprintf (stdout, h, "%g", "%g");
		gsl_histogram_free (h);
	}
	exit (0);
}

