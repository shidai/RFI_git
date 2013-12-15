#!/bin/sh
# calculate the flux, energy, width, occurance distributions

for (( i = 1; i <= 100; i = i + 1))
do
    export num_w=`awk '$3<='$i' && $3>'$i-1'' countRFI.txt | wc -l`
    echo "$i  $num_w" >> width.txt
done

for (( i = 20200; i <= 220000; i = i + 200))
do
    export num_p=`awk '$4<='$i' && $4>'$i-200'' countRFI.txt | wc -l`
    echo "$i  $num_p" >> peak.txt
done

for (( i = 20200; i <= 2200000; i = i + 200))
do
    export num_e=`awk '$5<='$i' && $5>'$i-200'' countRFI.txt | wc -l`
    echo "$i  $num_e" >> energy.txt
done

for (( i = 1; i <= 360; i = i + 1))
do
    awk '$6<='$i' && $6>'$i-1'' countRFI.txt > temp.txt 
    for (( j = 1; j <= 90; j = j + 1))
    do
        export num=`awk '$7<='$j' && $7>'$j-1'' temp.txt | wc -l` 
	echo "$i $j $num" >> az_el.txt
    done
done
