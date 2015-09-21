#!/usr/bin/env gnuplot
set datafile commentschars ";"

set terminal svg
set output "test.svg"

set multiplot layout 2,1
plot "test.dat" using 1:2 every 1000 with lines
plot ""         using 1:3 every 100 with lines
unset multiplot