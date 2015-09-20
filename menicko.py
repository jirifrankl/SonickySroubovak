#!/usr/bin/python

import os
#os.system("ls -l")
a=100
p1="napis cislo: \n 1: Playback_to_Headset.sh (sluchatka) \n 2: Playback_to_Lineout.sh (line out) \n 3: Playback_to_Speakers.sh (reproduktory) \n 4:Record_from_Headset.sh (nahravani ze sluchatek)	\n 5:Record_from_lineIn_Micbias.sh (zapnuti nahravani z line in) \n 6:Record_from_lineIn.sh (nahravani line in) \n 7:Reset_paths.sh (reset)\n 8:zapnuto vse \n 0:Konec"
p2="napis cislo: \n 1: sluchatka \n 2: line out \n 3: reproduktory \n 4: nahravani ze sluchatek	\n 5: zapnuti nahravani z line in \n 6: nahravani line in \n 7: reset \n 8: zapnuto vse \n 9: menicko \n 0: Konec "    
p=p2
while a!=0:
    
    print (p)
    #print("napis cislo: \n 1: sluchatka \n 2: line out \n 3: reproduktory \n 4: nahravani ze sluchatek	\n 5: zapnuti nahravani z line in \n 6: nahravani line in \n 7: reset \n 8: zapnuto vse \n 9: menicko \n 0: vse vypnuto ")
    #print("napis cislo: \n 1: Playback_to_Headset.sh (sluchatka) \n 2: Playback_to_Lineout.sh (line out) \n 3: Playback_to_Speakers.sh (reproduktory) \n 4:Record_from_Headset.sh (nahravani ze sluchatek)	\n 5:Record_from_lineIn_Micbias.sh (zapnuti nahravani z line in) \n 6:Record_from_lineIn.sh (nahravani line in) \n 7:Reset_paths.sh (reset)\n 8:zapnuto vse \n 0:vse vypnuto")
    


    a=int(input())

    if a==1:
       print("sluchatka")
       os.system("/home/pi/use_case_scripts/Playback_to_Headset.sh")
    elif a==2:
        print("line out")
        os.system("/home/pi/use_case_scripts/Playback_to_Lineout.sh")
    elif a==3:
        print("reproduktory")
        os.system("/home/pi/use_case_scripts/Playback_to_Speakers.sh")
    elif a==4:
         print("nahravani ze sluchatek")
         os.system("/home/pi/use_case_scripts/Record_from_Headset.sh")
    elif a==5:
        print("zapnuti nahravani z line in")
        os.system("/home/pi/use_case_scripts/Record_from_lineIn_Micbias.sh")   
    elif a==6:
        print("nahravani line in")
        os.system("/home/pi/use_case_scripts/Record_from_lineIn.sh")
    elif a==7:
         print("reset")
         os.system("/home/pi/use_case_scripts/Reset_paths.sh")
    elif a==8:
        print("vse")
        os.system("/home/pi/use_case_scripts/Playback_to_Headset.sh")
        os.system("/home/pi/use_case_scripts/Playback_to_Lineout.sh")
        os.system("/home/pi/use_case_scripts/Playback_to_Speakers.sh")
        os.system("/home/pi/use_case_scripts/Record_from_Headset.sh")
        os.system("/home/pi/use_case_scripts/Record_from_lineIn_Micbias.sh")
        os.system("/home/pi/use_case_scripts/Record_from_lineIn.sh")
    elif a==9:
        print(p)
    elif a==0:
        exit
    else:
         print("spatna volba")
    

