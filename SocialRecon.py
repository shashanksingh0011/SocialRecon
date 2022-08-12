import pyfiglet
from gtts import gTTS  
from playsound import playsound
import time
import sys
from pdfanalysis import pdfinfo
from iplocator import iplocate
from webscrap import Links
from number import number
from Instagraminfo import instainfo
R = '\033[31m' 
G = '\033[32m'
C = '\033[36m'
W = '\033[0m' 

def reconinput():
    inp=(input("social recon >> "))
    if (inp=='1'):
        iplocate()
    elif (inp=='2'):
        pdfinfo()
    elif(inp=='3'):
        Links()
    elif (inp=='4'):
        number()
    elif(inp=='5'):
        instainfo()
    elif(inp=='exit'):
        exit()
    else:
        text="please enter an valid option "
        aud=gTTS(text=text,lang=language,slow=False)
        aud.save("valid.mp3")
        playsound("valid.mp3")   
        
if __name__=="__main__":
    print(
            """ 
                     
     _____            _       _  ______                     
    /  ___|          (_)     | | | ___ \                    
    \ `--.  ___   ___ _  __ _| | | |_/ /___  ___ ___  _ __  
     `--. \/ _ \ / __| |/ _` | | |    // _ \/ __/ _ \| '_ \ 
    /\__/ | (_) | (__| | (_| | | | |\ |  __| (_| (_) | | | |
    \____/ \___/ \___|_|\__,_|_| \_| \_\___|\___\___/|_| |_|
           
            """
        )
    string="Tool created by - Rachana, Rashmika, Saba & Shalini"
    for char in string:
        print(char,end='')
        sys.stdout.flush()
        time.sleep(0.1)
    print()
    mytext = "Welcome to Social reconnaissance"
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    myobj.save("welcome.mp3") 
    playsound("welcome.mp3") 
    print('')
    print(C+"""Tools available 
    
            1.IP location Lookup
            2.PDF meta data analysis
            3.URL lookup
            4.Phonenumber verifier
            5.Instagram Info Lookup
            usage : type exit to stop
            """)
    print('')
    
    text="Please Select any tool "
    aud=gTTS(text=text,lang=language,slow=False)
    aud.save("options.mp3")
    playsound("options.mp3")   
    while True:
        reconinput()
