// find RFI with modified algorithm
// export azimuth and elevation
// include the energy of the RFI, which is the sum of all the RFI points
// include timeleg between utc and local time
// "width=0" bug corrected
// use 2.5 sigma as the width (half the peak)
// If only one point is above 2.5 sigma, then the width is set to be one, which means points on the edge below 2.5 sigma are not counted 
// remove the read function, and need one more parameter which tells the number of data points
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main (int argc, char *argv[])
{
	    // get the number of data points
		int npoints;

		npoints=atoi(argv[9]);
        // get the timeleg
        float timeleg;
        
        timeleg=atof(argv[8]);

        // get the information of azimuth and elevation
	float azstart,azend,elstart,elend,fnum,fn;
     
        azstart=atof(argv[2]);
        azend=atof(argv[3]);

        elstart=atof(argv[4]);
        elend=atof(argv[5]);

        fnum=atof(argv[6]);
        fn=atof(argv[7]);

        float azstep,elstep;
        azstep=(azend-azstart)/fnum;
        elstep=(elend-elstart)/fnum;

        float azimuth,elevation;
        azimuth=azstart+(fn-1.0)*azstep;
        elevation=elstart+(fn-1.0)*elstep;

	int num;

	num=npoints;
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

	int i,j,h;
	float x;

	// printf ("%d\n", i);
	float ave;
        //ave=33603.843750;

        ave=0.0;
	i=0;
	//while (fscanf (fp, "%f %f %f", &xx, &x, &xxx) == 3)
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
        //devi=474.631989;
	devi=0.0;
	for (i=0;i<num;i++)
	{
		devi+=(data[i]-ave)*(data[i]-ave);
	}
	devi=sqrt(devi/num);

	//printf ("%f %f\n", ave, devi);

        int plus, minus;
	int start,end,width,peak;
        float energy;
	for (i=0;i<num;i++)
	{
                //printf ("%d\n",i);
		if (i>0 && (data[i]-ave)>=(5.0*devi))
	            //printf ("%f\n", data[i]);
		{
                    plus=0;
                    minus=0;
		    if (data[i-1]<data[i] && data[i+1]<data[i])
	            {	
                        j=1;

                        while ((i+j)<num && data[i]>data[i+j])
                        {
                            if ( (data[i+j]-ave)<=2.5*devi )
                            {
                                plus=1;
                                break; 
                            }
                            j++;
                        }

                        j=1;

                        while ((i-j)>=0 && data[i]>data[i-j])
                        {
                            if ( (data[i-j]-ave)<=2.5*devi )
                            {
                                minus=1;
                                break;
                            }
                            j++;
                        }

		    }
		    //printf ("%d\n", j);

		    if (plus==1 && minus==1)
		    {

		        peak=i;   // if data[i] is the local max, peak=i
                        start=i;
                        end=i;

                        energy=0.0;
		        for(h=0;h<i;h++)
		        {
		            if ((i-h)<=0 || (data[i-h]-ave)<=2.5*devi)
			    {
			        break;
			    }
		            start=i-h;  // start of the spike
                            energy+=data[i-h];
		        }

		        for(h=1;h<num;h++)
		        {
		            if ((i+h)>=num || (data[i+h]-ave)<=2.5*devi)
			    {
			        //printf ("%d %d %f %f\n", i, i+h, data[i+h], (data[i+h]-ave)/devi);
			        break;
			    }
			    end=i+h;  // end of the spike
                            energy+=data[i+h];
	                }
			width=end-start+1;
		    
			printf ("%s %d %d %f %f %f %f %f\n", argv[1], peak, width, data[i], energy, azimuth, elevation, timeleg);
		    }
		}
		else if (i==0 && (data[i]-ave)>=(5.0*devi))
		{
                    plus=0;
		    if (data[i+1]<data[i])
	            {	
                        j=1;

                        while ((i+j)<num && data[i]>data[i+j])
                        {
                            if ( (data[i+j]-ave)<=2.5*devi )
                            {
                                plus=1;
                                break; 
                            }
                            j++;
                        }
                    }

		    if (plus==1)
		    {
			peak=0;
                        start=0;
                        end=0;

                        energy=0.0;
		        for(h=0;h<num;h++)
		        {
		            if ((i+h)>=num || (data[i+h]-ave)<=2.5*devi)
			    {
			        //printf ("%d %f %f\n", i+h, data[i+h], (data[i+h]-ave)/devi);
			        break;
			    }
			        //printf ("%d %f %f\n", i+h, data[i+h], (data[i+h]-ave)/devi);
			    end=h;  // start of the spike
                            energy+=data[i+h];
	                }
			width=end-start+1;
		    
			printf ("%s %d %d %f %f %f %f %f\n", argv[1], peak, width, data[i], energy, azimuth, elevation, timeleg);
		    }
		}
	}

	free(data);
	if (fclose (fp) != 0)	
	    fprintf (stderr, "Error closing\n");
	
	return 0;
}
    	
