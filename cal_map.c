// calculate map of RFI
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main (int argc, char *argv[])
{
	// read data 
    FILE *fp;
	if ((fp = fopen(argv[1], "r")) == NULL)
	{
		fprintf (stdout, "Can't open file\n");
		exit(1);
	}


	// printf ("%d\n", i);
	float az,el;
        int i,n,norm;

        float r;
        float x,y;

        i=0;
	while (fscanf (fp, "%f %f %d %d", &az, &el, &n, &norm) == 4)
		{
			r=cos(el*3.1415926/180.0);
                        x=r*cos((az-90)*3.1415926/180.0);
                        y=-r*sin((az-90)*3.1415926/180.0);
                        //x=r*cos((az+90)*3.1415926/180.0);
                        //y=r*sin((az+90)*3.1415926/180.0);
			if (n>0)
			{
				printf ("%f %f %d\n", x, y, n/norm);
			}
			else
			{
				printf ("%f %f %d\n", x, y, n);
			}
			i++;
                        if ((i%360)==0)
			    printf ("\n");
		}

	if (fclose (fp) != 0)	
	    fprintf (stderr, "Error closing\n");
	
	return 0;
}
    	
