#!/bin/sh

gnuplot <<- EOF

set terminal post eps color enhanced 
set output 'month.ps'

set xrange [0:12]
set xlabel 'Month'
set xtics ("1" 0.5, "2" 1.5, "3" 2.5, "4" 3.5, "5" 4.5, "6" 5.5, "7" 6.5, "8" 7.5, "9" 8.5, "10" 9.5, "11" 10.5, "12" 11.5)
#set mxtics 2
set ylabel 'N'
#set ytics 1
#set mytics 5
plot 'result' using 1:2 w lines title ''

EOF
