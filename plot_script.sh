#!/bin/sh

#gnuplot  -persist  << EOF
gnuplot  <<- EOF

set term post eps color
set output 'occurance.ps'

set style data histogram
set style fill solid 0.4 border
set style histogram clustered gap 0
#set style histogram gap 0

set xlabel '(local time)'
unset key
set multiplot layout 1,3 title "2010-08-22"

set lmargin 2
set rmargin 0
set xrange [0:17]
set yrange [0:80000]
set ytics axis  
set xtics axis  
set ytics 40000
set mytics 2
set ytics rotate by 90
set xtics 8
set xtics ("" 0, "13:42 -- 16:29" 8, "" 16)
plot 'part11' u 3, '' u 4
#plot 'part1' u 3 lc 1

set lmargin 0
set xrange [-1:20]
unset ytics
set xtics 10
set xtics ("" -1, "19:42 -- 23:01" 9, "" 19)
plot 'part22' u 3, '' u 4 
#plot 'part2' u 3 lc 2

set rmargin 2
set xrange [0:28]
set xtics 15
set xtics ("" 0, "04:57 -- 09:32" 15, "" 28)
set key
plot 'part33' u 3 title '5 \sigma', '' u 4 title '10 \sigma'
#plot 'part3' u 3 lc 3

EOF
