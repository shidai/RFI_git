#!/bin/sh

for (( i = 1; i <= 50; i = i + 1))
do
    export num=`awk '$3<='$i' && $3>'$i-1'' countRFI.txt | wc -l`
	echo "$i  $num"
done
