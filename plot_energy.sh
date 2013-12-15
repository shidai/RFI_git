#!/bin/sh

gnuplot <<- EOF

set terminal post eps color enhanced 
set output 'energy.ps'

set xrange [0:10.5]
set xlabel 'energy (Jy)'
#set xlabel 'energy (K)'
set xtics 1
set mxtics 5
set yrange [2:6.5]
set ylabel 'log10(N)'
set ytics 1
set mytics 5
plot 'result' using ((\$1)*0.000006553):(log10(\$2)) w lines title ''
#plot 'result' using ((\$1)*0.000004745):(log10(\$2)) w lines title ''

EOF
