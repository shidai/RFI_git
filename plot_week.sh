#!/bin/sh

gnuplot <<- EOF

set terminal post eps color enhanced 
set output 'week_norm.ps'
#set output 'week.ps'

set xrange [0:7]
set xlabel 'Week'
set xtics ("Mon." 0.5, "Tues." 1.5, "Wed." 2.5, "Thur." 3.5, "Fri." 4.5, "Sat." 5.5, "Sun." 6.5)
#set mxtics 2
set ylabel 'N'
#set ytics 1
#set mytics 5
plot 'result_norm' using 1:2 w lines title ''
#plot 'result' using 1:(log10(\$2)) w lines title ''

EOF
