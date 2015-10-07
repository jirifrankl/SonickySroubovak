#!/usr/bin/env gnuplot
set datafile commentschars ";"

set terminal svg
set output "test.svg"

set multiplot layout 3,1

set ylabel "sample value"
set bmargin 0
set format x ""
set ytics -0.8,0.2
set key bottom
#plot [0.2:1] "test.dat" using 1:2 every 1000 with lines lc rgbcolor "#a0a0b0" #title "left channel"

set xlabel "time (s)"
set bmargin
set tmargin 0
set format x "%g"
set format y "%g"
set ytics -1.0,0.2,0.8
set key top

plot [0.48:0.485] "440-cd3.dat"            using 1:3 with lines lc rgbcolor "#a0a1b1" #title "right channel"
plot [0.48:0.485] "test.dat"                using 1:3 with lines lc rgbcolor "#a0a1b1" #title "right channel"
set ylabel "sample value r"
set ytics -0.01,0.02,0.08
plot [0.49:0.5] "test2.dat"       using 1:3 with lines lc rgbcolor "#a0a1b1" #title "right channel"
unset multiplot