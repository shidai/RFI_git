#!/bin/bash

for month in 1 2 3 4 5 6 7 8 9 10 11 12; do
	num=`awk -F "-" '$2=='$month'' ../countRFI.txt | awk -F "/" '{print $11}' | awk '{print $1}' | uniq | wc -l`
	echo $num
done
