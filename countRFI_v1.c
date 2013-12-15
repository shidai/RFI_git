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
//int readbinary ( char *filename, int *ntxt, double *x, double *y )
{
	int num;

	// get the number of points
	read(&num,argv[1]);

	// arrange a space to store the data
	float *data;
	data=(float *)malloc(sizeof(float)*num);
	
	// read data 
    FILE *fp;
	if ((fp = fopen(argv[1], "r")) == NULL)
	{
		fprintf (stdout, "Can't open file\n");
		exit(1);
	}

	int i,j,jj,h;
	float x;

	// printf ("%d\n", i);
	float ave;

	ave=0.0;
	i=0;
	while (fread (&x, sizeof(float), 1, fp) == 1)
		{
			data[i]=x;
			//puts (c);
			//printf ("%s %f %f\n", name[i], x[i], y[i]);
			ave+=data[i];
			i++;
		}
	ave=ave/num;
	//printf ("number of point: %d\n", i);

	float devi;
	devi=0.0;
	for (i=0;i<num;i++)
	{
		devi+=(data[i]-ave)*(data[i]-ave);
	}
	devi=sqrt(devi/num);

	//printf ("%f %f\n", ave, devi);

	int start,end,width,peak;
	for (i=0;i<num;i++)
	{
		if (i>20 && (data[i]-ave)>(10.0*devi))
	            //printf ("%f\n", data[i]);
		{
		    for(j=1;j<20;j++)
		    {
		        if (data[i-j]>data[i] || data[i+j]>data[i])
			{
			    break;
			}
		    }
		    //printf ("%d\n", j);

		    if (j==20)
		    {

		        peak=i;   // if data[i] is the local max, peak=i
                        start=i;
                        end=i;

		        for(h=0;h<20;h++)
		        {
		            if ((data[i-h]-ave)<0.0)
			    {
				start=i-h;  // start of the spike
			        break;
			    }
		        }

		        for(h=1;h<20;h++)
		        {
		            if ((data[i+h]-ave)<0.0)
			    {
				end=i+h;  // end of the spike
			        break;
			    }
	                }
			width=end-start;
		    
			printf ("%s %d %d %f\n", argv[1], peak, width, data[i]);
		    }
		}
		else if (i<20 && (data[i]-ave)>(10.0*devi))
		{
		    for(j=1;j<i;j++)
		    {
		        if (data[i-j]>data[i])
			{
			    break;
			}
		    }
		    //printf ("%d\n", j);
		    for(jj=1;jj<20;jj++)
		    {
		        if (data[i+jj]>data[i])
			{
			    break;
			}
		    }

		    if (j==i && jj==20)
		    {
			peak=i;
                        start=i;
                        end=i;

		        for(h=0;h<i;h++)
		        {
		            if ((data[i-h]-ave)<0.0)
			    {
				start=i-h;  // start of the spike
			        break;
			    }
		        }

		        for(h=1;h<20;h++)
		        {
		            if ((data[i+h]-ave)<0.0)
			    {
				end=i+h;  // start of the spike
			        break;
			    }
	                }
			width=end-start;
		    
			printf ("%s %d %d %f\n", argv[1], peak, width, data[i]);
		    }
		}
	}

	free(data);
	if (fclose (fp) != 0)	
	    fprintf (stderr, "Error closing\n");
	
	return 0;
}
    	
