#!/bin/sh

for (( i = 110; i <= 600; i = i + 10))
do
    export num=`awk '$3<='$i' && $3>'$i-10'' standard_deviation.txt | wc -l`
	echo "$i  $num"
done
