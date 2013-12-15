#!/bin/sh

gnuplot <<- EOF

set terminal post eps color  
set output 'test.ps'

set lmargin at screen 0.05
set rmargin at screen 0.85
set bmargin at screen 0.1
set tmargin at screen 0.9
set pm3d map 
#set pm3d map interpolate 20,20
unset key

set multiplot

# plot the heatmap

#set cntrparam levels increment 3,-3, -24
#set contour surface
set palette rgb 33,13,10 #rainbow (blue-green-yellow-red)
#set cbrange [-18:0]
unset border
#unset xtics
#unset ytics
set angles degree
#set colorbox user origin 0.9,0.1 size 0.03,0.8
splot 'dat.txt' using 1:2:3

# now plot the polar grid only
set polar
set grid polar  
set grid ls 0  
set style line 11 lc rgb 'black' lw 3 lt 0

r = 1.0
set xrange[-r:r]
set yrange[-r:r]

set xtics axis         #disply the xtics on the axis instead of on the border
set ytics axis

set xtics 0,0.2,1      #set the xtics only go from 0 to 1 with increment of 0.2 but do not display anything. 
set xtics format '' scale 0            #"remove" the tics so that only the y tics are displayed
#set xtics ("" 0, "" 0.2, "" 0.4, "" 0.6, "" 0.8, "" 1)
set ytics 0,0.2,1  #make the ytics go from the center 0 to 1 with incrment of 0.2

set for [i=0:330:30] label at first (r+0.1)*cos(i), first (r+0.1)*sin(i) center sprintf('%d', i)

plot NaN w l       # "plot Nan" only plot the polar grid

EOF
