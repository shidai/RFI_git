#!/bin/sh

gnuplot <<- EOF

set terminal post eps color enhanced 
set output 'energy_log.ps'

set logscale x
set xrange [0.013:1]
set xlabel 'log10(energy) (mJy s)'
#set xlabel 'energy (K)'
set xtics 0.1
set mxtics 5
set yrange [3:7]
set ylabel 'log10(N)'
set ytics 1
set mytics 5
plot 'result_log' using ((10**(\$1))*0.000006553*64/1000):(log10(\$2)) w lines title ''
#plot 'result' using ((\$1)*0.000004745):(log10(\$2)) w lines title ''

EOF
