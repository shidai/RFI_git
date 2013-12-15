#!/bin/sh

for (( i = 20200; i <= 220000; i = i + 200))
do
    export num=`awk '$4<='$i' && $4>'$i-200'' countRFI.txt | wc -l`
	echo "$i  $num"
done
