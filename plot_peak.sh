#!/bin/sh

gnuplot <<- EOF

set terminal post eps color enhanced 
#set output 'test.ps'
set output 'peak_log.ps'

set logscale x
#set logscale y
set xrange [0.2:0.95]
set xlabel 'log10(peak) (Jy)'
set xtics ("0.2" 0.2, "0.3" 0.3, "0.4" 0.4, "0.5" 0.5, "0.6" 0.6, "0.7" 0.7, "0.8" 0.8, "0.9" 0.9)
set yrange [0.5:6.5]
set ylabel 'log10(N)'
set ytics 1
set mytics 5
#plot 'result_log' using 1:(log10(\$2)) w lines title ''
#plot 'result' using 1:(log10(\$2+1)) w lines title ''
plot 'result_log' using (10**(\$1)*0.000006553):(log10(\$2)) w lines title ''

EOF
