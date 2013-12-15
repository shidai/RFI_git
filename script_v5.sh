#!/bin/bash
# add counting RFI for sub-blocks and rms calculations
# add the azimuth and elevation
# new directory structure
# add readfile.out, which returns the number of points
# countRFI.out now needs one more parameter, the number of data points
# add basic_info, which shows the average, sigma and rms of each beam

export route="../lustre/projects/p002_swin/surveys/HTRU/medlat"
ls -l $route/ | grep '2009' | awk '{print $9}' > list
export num=`ls -l $route/ | grep '2009' | wc -l`

for (( i = 1; i <= $num; i = i+1 ))
do
    export dir=`sed -n "$i"p list`
    #echo $dir

    # get the time of each directory
    #echo $dir | awk -F "-" '{print $4}' | awk -F "." '{print $1}' | awk -F ":" '{print $1,$2,$3}' > time
    #export hour=`sed -n '1p' time | awk '{print $1}'`
    #export minute=`sed -n '1p' time | awk '{print $2}'`
    #export second=`sed -n '1p' time | awk '{print $3}'`
    #export time_count=$(((10#$hour)*60*60+(10#$minute)*60+(10#$second)))
 
    # get the information of azimuth and elevation, which is the same for every beams in a 10min block 
    # use the .psrxml under 01 directory

    # get the start and end of azimuth and elevation
    export azstart=`cat $route/$dir/01/*.psrxml | grep az | awk -F ">" '{print $2}' | awk -F "<" '{print $1}' | sed -n 1p` 
    export azend=`cat $route/$dir/01/*.psrxml | grep az | awk -F ">" '{print $2}' | awk -F "<" '{print $1}' | sed -n 2p` 

    export elstart=`cat $route/$dir/01/*.psrxml | grep "<el" | awk -F ">" '{print $2}' | awk -F "<" '{print $1}' | sed -n 1p` 
    export elend=`cat $route/$dir/01/*.psrxml | grep "<el" | awk -F ">" '{print $2}' | awk -F "<" '{print $1}' | sed -n 2p` 

    # get the time difference between utc and local time
    export timeleg=`cat $route/$dir/01/*.psrxml | grep local_time | awk -F "+" '{print $2}' | awk -F "<" '{print $1}'` # hour
    #echo $timeleg;


    for (( j = 1; j <= 13; j = j+1 ))
    do
        if [[ $timeleg != 10 && $timeleg != 11 ]]; then
            echo "$dir wrong data" 
            break
        fi

        if [ $j -lt 10 ]; then
	    export beam=0$j
	    #echo $beam
	    else
	    export beam=$j
	    #echo $beam
	fi
	
        test ! -f $route/$dir/$beam/aux.tar && echo "no file" || test -f $route/$dir/$beam/aux.tar && test -d $route/$dir/$beam/aux && echo "tared" || test -f $route/$dir/$beam/aux.tar && test ! -d $route/$dir/$beam/aux && tar --force-local -xf $route/$dir/$beam/aux.tar -C $route/$dir/$beam/ 

        ls -l $route/$dir/$beam/aux/ | grep ts0 | awk '{print $9}' > dataname
	#ls -l $dir/$beam/aux/ | grep ts0 | awk '{print $9}' | awk -F "-" '{print $4}' | awk -F "." '{print $1}' | awk -F ":" '{print $1,$2,$3}' > time
        export fnum=`ls -l $route/$dir/$beam/aux/ | grep ts0 | wc -l`
	#echo $fnum

	# create the file to store results for each beam
	#export beamfile=$beam.txt
	#export beamresult="$beam"result.txt

        for (( h = 1; h <= $fnum; h = h+1 ))
        do
            export name=`sed -n "$h"p dataname`
	    #echo $name
            #export hour=`sed -n "$h"p time | awk '{print $1}'`
	    #echo $hour
            #export minute=`sed -n "$h"p time | awk '{print $2}'`
            #export second=`sed -n "$h"p time | awk '{print $3}'`
	    #./baseline.out ../$dir/$beam/aux/$name >> baseline"$beam".txt
	    #baseline.out $dir/$beam/aux/$name $hour $minute $second >> baseline"$beam".txt
	    #RFI.out $dir/$beam/aux/$name >> RFI.txt

            # get the number of data points in the file
            export numpoint=`./readfile.out $route/$dir/$beam/aux/$name`

            # output RFI information, including the azimuth and elevation for each sub-blocks
	    ./countRFI.out $route/$dir/$beam/aux/$name $azstart $azend $elstart $elend $fnum $h $timeleg $numpoint >> countRFI.txt       # output results to one file
	    #./countRFI.out ../$dir/$beam/aux/$name >> ./beam/$beamfile    # output results to files of each beam
	    
	    #./standard_deviation.out $dir/$beam/aux/$name >> standard_deviation.txt
	    #./rms.out ../$dir/$beam/aux/$name >> rms.txt

	    ./basic_info.out $route/$dir/$beam/aux/$name $numpoint $beam >> basic_info.txt       # output results to one file
            # count occurance for each sub-blocks 
            #export subname="../$dir/$beam/aux/$name"
            #export num_block=`cat countRFI.txt | grep $subname | wc -l`
            #echo "$subname   $num_block" >> num_block.txt

        done 

        rm -rf $route/$dir/$beam/aux/

        # count occurace of each beam

        #export num_count=`cat ./beam/$beamfile | grep $dir | wc -l`
        #echo "$time_count  $num_count"  >> ./beam/$beamresult

    done

    # count occurance 

    export num_count=`cat countRFI.txt | grep $dir | wc -l`
    echo "$dir  $num_count $timeleg"  >> result.txt

done
