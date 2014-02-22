#!/bin/bash

for name in `awk -F "/" '{print $8}' ../countRFI.txt | awk -F ":" '{print $1}' | uniq`; do
	num=`cat ../countRFI.txt | grep $name | awk -F "/" '{print $11}' | awk '{print $1}' | uniq | wc -l`
	leg=`cat ../countRFI.txt | grep $name | tail -1 | awk '{print $8}'`
	year=`echo $name | awk -F "-" '{print $1}'`
	month=`echo $name | awk -F "-" '{print $2}'`
	day=`echo $name | awk -F "-" '{print $3}'`
	hour=`echo $name | awk -F "-" '{print $4}'`
	echo "$year $month $day $hour $num $leg"
#	echo "$name $num"
done
