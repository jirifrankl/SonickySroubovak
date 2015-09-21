#!/bin/bash
#Vytvori sinusoidovy zaznam s frekvenci danou prvnim parametrem za sin vzorkovaci frekvenci  44100
 
sox -n -c 2 -r    44100 -b 16  440-cd3.wav synth 0.5 sin 11533  gain -3

#prevede waw soubor do souboru dat
sox 440-cd3.wav test.dat


