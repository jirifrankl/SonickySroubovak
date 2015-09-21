arecord -d 1 -Dhw:sndrpiwsp -r 44100 -c 2 -f S16_LE out.wav &

aplay -Dhw:sndrpiwsp -r 44100 -c 2 -f S16_LE 440-cd3.wav

sox  out.wav test.dat



