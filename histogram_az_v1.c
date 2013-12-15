#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main (int argc, char *argv[])
{
	if (argc != 2)
	{
		printf ("Usage: gsl-histogram xmin xmax n\n"
			"Computes a histogram of the data "
			"on stdin using n bins from xmin "
			"to xmax\n");
		exit (0);
	}

	int count[360][90];

	int i,j;
	for (i = 0; i < 360; i++)
	{
	    for (j = 0; j < 90; j++)
		{
		    count[i][j] = 0;
		}
	}

	{
		float x,y;
		int xx,yy;

		FILE *fp;
		if ((fp = fopen(argv[1], "r")) == NULL)
		{
			fprintf (stdout, "Can't open file\n");
			exit(1);
		}

		while (fscanf (fp, "%f %f", &x, &y) == 2)
		{
			xx = x;
			yy = y;

			count[xx][yy] += 1;
		}
		//printf ("%d\n", index);
	
		if (fclose (fp) != 0)
			fprintf (stderr, "Error closing\n");

		for (i = 0; i < 360; i++)
		{
		    for (j = 0; j < 90; j++)
			{
				printf ("%d %d %d\n", i, j, count[i][j]);
			}
		}

	}

	return 0;
}

