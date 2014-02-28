#!/bin/bash
# add counting RFI for sub-blocks and rms calculations
# add the azimuth and elevation
# new directory structure
# add readfile.out, which returns the number of points
# countRFI.out now needs one more parameter, the number of data points
# add basic_info, which shows the average, sigma and rms of each beam
# version control by git

# only beam 04
export beam=04
	
while read filename; do
 
find /lustre/projects/p002_swin/surveys/HTRU/medlat/"$filename"-*/$beam/ -name aux.tar | xargs tar -cf data.tar
find /lustre/projects/p002_swin/surveys/HTRU/medlat/"$filename"-*/$beam/ -name *.psrxml | xargs tar -cf psrxml.tar

tar -xf data.tar
rm data.tar
tar -xf psrxml.tar
rm psrxml.tar

export route="./lustre/projects/p002_swin/surveys/HTRU/medlat"
ls -l $route/ | awk '{print $9}' > list
export num=`cat list | wc -l`

for (( i = 1; i <= $num; i = i+1 ))
do
    export dir=`sed -n "$i"p list`
    #echo $dir

    # get the information of azimuth and elevation, which is the same for every beams in a 10min block 
    # use the .psrxml under 01 directory

    # get the start and end of azimuth and elevation
    export azstart=`cat $route/$dir/$beam/*.psrxml | grep az | awk -F ">" '{print $2}' | awk -F "<" '{print $1}' | sed -n 1p` 
    export azend=`cat $route/$dir/$beam/*.psrxml | grep az | awk -F ">" '{print $2}' | awk -F "<" '{print $1}' | sed -n 2p` 

    export elstart=`cat $route/$dir/$beam/*.psrxml | grep "<el" | awk -F ">" '{print $2}' | awk -F "<" '{print $1}' | sed -n 1p` 
    export elend=`cat $route/$dir/$beam/*.psrxml | grep "<el" | awk -F ">" '{print $2}' | awk -F "<" '{print $1}' | sed -n 2p` 

    # get the time difference between utc and local time
    export timeleg=`cat $route/$dir/$beam/*.psrxml | grep local_time | awk -F "+" '{print $2}' | awk -F "<" '{print $1}'` # hour
    #echo $timeleg;


    if [[ $timeleg != 10 && $timeleg != 11 ]]; then
    	echo "$dir wrong data" 
        continue
    fi

    test ! -f $route/$dir/$beam/aux.tar && echo "no file" || test -f $route/$dir/$beam/aux.tar && test -d $route/$dir/$beam/aux && echo "tared" || test -f $route/$dir/$beam/aux.tar && test ! -d $route/$dir/$beam/aux && tar --force-local -xf $route/$dir/$beam/aux.tar -C $route/$dir/$beam/ 

    ls -l $route/$dir/$beam/aux/ | grep ts0 | awk '{print $9}' > dataname
    export fnum=`ls -l $route/$dir/$beam/aux/ | grep ts0 | wc -l`
    #echo $fnum

    for (( h = 1; h <= $fnum; h = h+1 ))
    do
        export name=`sed -n "$h"p dataname`

        # get the number of data points in the file
        export numpoint=`./readfile.out $route/$dir/$beam/aux/$name`

		export mean=`./cal_mean.out $route/$dir/$beam/aux/$name $numpoint` 

		export up=`cat mean_beam | grep beam$bn | awk '{print $2}' | awk -F "-" '{print $1}'`
		export down=`cat mean_beam | grep beam$bn | awk '{print $2}' | awk -F "-" '{print $2}'`

		if [[ $mean >= $down && $mean <= $up ]]; then
			# output RFI information, including the azimuth and elevation for each sub-blocks
			./countRFI.out $route/$dir/$beam/aux/$name $azstart $azend $elstart $elend $fnum $h $timeleg $numpoint >> "$filename"_countRFI.txt       # output results to one file
	    
			./basic_info.out $route/$dir/$beam/aux/$name $numpoint $beam >> "$filename"_basic_info.txt       # output results to one file
		fi
    done 

    rm -rf $route/$dir/$beam/

    # count occurance 

    export num_count=`cat "$filename"_countRFI.txt | grep $dir | wc -l`
    echo "$dir  $num_count $timeleg"  >> "$filename"_result.txt

done

rm -rf ./lustre/

done < input
