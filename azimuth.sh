#!/bin/sh

for (( i = 1; i <= 360; i = i + 1))
do
    awk '$5<='$i' && $5>'$i-1'' countRFI.txt > temp.txt 
    for (( j = 1; j <= 90; j = j + 1))
    do
        export num=`awk '$6<='$j' && $6>'$j-1'' temp.txt | wc -l` 
	echo "$i $j $num"
    done
done
