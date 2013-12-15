#!/bin/sh

gnuplot <<- EOF

set terminal post eps color enhanced 
set output 'test.ps'
#set output 'peak.ps'

#set xrange [0:0.95]
#set xlabel 'peak (Jy)'
#set xtics 0.1
#set mxtics 5
#set yrange [0:5.5]
#set ylabel 'log10(N)'
#set ytics 1
#set mytics 5
plot 'result' using 1:2 w lines title ''
#plot 'result' using 1:(log10(\$2+1)) w lines title ''
#plot 'result' using ((\$1)*0.000006553):(log10(\$2+1)) w lines title ''

EOF
