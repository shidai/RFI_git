#!/bin/sh

export time=`awk '{print $3}' result.txt | sed -n 1p`
for (( i = 0; i <= 23; i = i + 1 ))
do
    export n2=`awk -F "-" '{print $4}' result.txt | awk -F ":" '$1=='$i' && $2>30' | wc -l`
    export num2=0
    for (( j = 1; j <= $n2; j = j + 1 ))
    do 
        export temp=`awk -F "-" '{print $4}' result.txt | awk -F ":" '$1=='$i' && $2>30' | awk '{print $2}' | sed -n "$j"p`
        export num2=$(( $num2 + $temp ))
    done

    export n1=`awk -F "-" '{print $4}' result.txt | awk -F ":" '$1=='$i' && $2<=30' | wc -l`
    export num1=0
    for (( j = 1; j <= $n1; j = j + 1 ))
    do 
        export temp=`awk -F "-" '{print $4}' result.txt | awk -F ":" '$1=='$i' && $2<=30' | awk '{print $2}' | sed -n "$j"p`
        export num1=$(( $num1 + $temp ))
    done


    export hour=$(( $i + $time ))
    if [ $hour -gt 23 ];then
        export hour=$(( $hour - 24 ))
    fi

    echo "$hour   $num1"
    echo "$hour.5 $num2"
done
