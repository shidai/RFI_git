// 2014.02.28: using an iterative method to calculate the mean and standard deviation of each data block.
// Return the mean and standard deviation, which can be used to kick out bad data blocks.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int cal_devi(float *data, int num, float *ave, float *devi)
// using an iterative definition of the standard deviation; calculating the mean and standard deviation
{
	float mean;
	float sigma;

	int i;
	mean=0.0;
	for (i=0;i<num;i++)
	{
		mean = mean + data[i];
	}
	mean=mean/num;

	sigma=0.0;
	for (i=0;i<num;i++)
	{
		sigma+=(data[i]-mean)*(data[i]-mean);
	}
	sigma=sqrt(sigma/num);

	//printf ("%f %f\n", ave, devi);
	
	(*ave)=mean;
	(*devi)=sigma;

	return 0;
}

int main(int argc, char *argv[])
{
	// open file 
    FILE *fp;
	if ((fp = fopen(argv[1], "r")) == NULL)
	{
		fprintf (stdout, "Can't open file\n");
		exit(1);
	}

	// get the number of data points
	int i;
	i=0;

	float z,x,zz,zzz;
	while (fscanf (fp, "%f %f %f %f", &z,&x,&zz,&zzz) == 4)
	{
		i++;
	}
	int num=i;
	//printf ("number of point: %d\n", i);
	
    if (fclose (fp) != 0)
		fprintf (stderr, "Error closing\n");

	///////////////////////////////////////////////////////////////////////////
	///////////////////////////////////////////////////////////////////////////
	
	// arrange a space to store the data
	float *data;
	data=(float *)malloc(sizeof(float)*num);
	
	// open file 
	if ((fp = fopen(argv[1], "r")) == NULL)
	{
		fprintf (stdout, "Can't open file\n");
		exit(1);
	}

	i=0;
	// read data
	while (fscanf (fp, "%f %f %f %f", &z,&x,&zz,&zzz) == 4)
	{
		data[i]=x;
		i++;
	}

	// close file
	if (fclose (fp) != 0)	
	    fprintf (stderr, "Error closing\n");

	///////////////////////////////////////////////////////////////////////////
	///////////////////////////////////////////////////////////////////////////
	
	// initialize
	float mean,sigma;
	float mean0,sigma0;
	cal_devi(data, num, &mean, &sigma);
	//printf ("%.2lf %.2lf\n", mean, sigma);

	mean0=mean;
	sigma0=sigma;

	int count1=0;
	int count2=0;

	int j=0;
	for (i=0;i<num;i++)
	{
		if (fabs(data[i]-mean) >= sigma)
		//if (fabs(data[i]-mean)/5 >= sigma)
		{
			count1++;
		}
		else
		{
			j++;
		}
	}

	while (count1>count2)
	{
		float *temp;
		temp=(float *)malloc(sizeof(float)*j);

		count2=0;
		j=0;
		for (i=0;i<num;i++)
		{
			if (fabs(data[i]-mean) >= sigma)
			//if (fabs(data[i]-mean)/5 >= sigma)
			{
				count2++;
			}
			else
			{
				temp[j] = data[i];
				j++;
			}
		}

		cal_devi(temp, j, &mean, &sigma);
		//printf ("%.2lf %.2lf\n", mean, sigma);

		count1=0;
		j=0;
		for (i=0;i<num;i++)
		{
			if (fabs(data[i]-mean)/5 >= sigma)
			{
				count1++;
			}
			else
			{
				j++;
			}
		}

		free(temp);
	}

	printf ("%.2lf-%.2lf\n", mean-sigma, mean+sigma);
	//printf ("%.2lf %.2lf %.2lf %.2lf\n", mean0, sigma0, mean, sigma);

	free(data);

	return 0;
}

