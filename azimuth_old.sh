#!/bin/bash

for (( i = 1; i <= 360; i = i + 1))
do
    awk '$6<='$i' && $6>'$i-1'' './countRFI.txt' > temp.txt 
    for (( j = 1; j <= 90; j = j + 1))
    do
        export num=`awk '$7<='$j' && $7>'$j-1'' temp.txt | wc -l` 
        export norm=`awk '$7<='$j' && $7>'$j-1' {print $1}' temp.txt | uniq | wc -l` 
	echo "$i $j $num $norm"
    done
#	echo " "
done
