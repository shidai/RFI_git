#!/bin/sh

gnuplot <<- EOF

set terminal post eps color enhanced 
set output 'occurance_new.ps'

set xrange [0:24]
set xlabel 'Local time'
set xtics 1
set mxtics 2
set ylabel 'N'
#set ytics 1
#set mytics 5
plot 'result2' using ((\$1)/2):2 w lines title ''
#plot 'result' using 1:(log10(\$2)) w lines title ''
#plot 'result' using ((\$1)*64/1000):(log10(\$2)) w lines title ''

EOF
