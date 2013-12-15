#!/bin/sh

gnuplot <<- EOF

set terminal post eps color enhanced 
set output 'width.ps'

#set xlabel 'Width (ms)'
set xlabel 'Width (64 {/Symbol m}s)'
set xtics 5
set mxtics 5
set ylabel 'log10(N)'
set ytics 1
set mytics 5
plot 'result' using 1:(log10(\$2)) w lines title ''
#plot 'result' using ((\$1)*64/1000):(log10(\$2)) w lines title ''

EOF
