#!/bin/sh

gnuplot <<- EOF

set terminal post eps color enhanced 
set output 'width_log.ps'
#set output 'width_new.ps'

#set xlabel 'Width (ms)'
set xlabel 'log(width) (64 {/Symbol m}s)'
set xtics 1
set mxtics 10
set ylabel 'log10(N)'
set ytics 1
set mytics 5
plot [0:3] 'result_log' using 1:(log10(\$2)) w lines title ''
#plot 'result' using ((\$1)*64/1000):(log10(\$2)) w lines title ''

EOF
