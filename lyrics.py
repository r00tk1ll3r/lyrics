#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import sys

banner = '''
██╗  ██╗   ██╗██████╗ ██╗ ██████╗███████╗
██║  ╚██╗ ██╔╝██╔══██╗██║██╔════╝██╔════╝
██║   ╚████╔╝ ██████╔╝██║██║     ███████╗
██║    ╚██╔╝  ██╔══██╗██║██║     ╚════██║
███████╗██║   ██║  ██║██║╚██████╗███████║
╚══════╝╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝╚══════╝
                                         
Script Written By r00tk1ll3r

To See Useage just execute python3 lyrics.py
'''

print(banner)

useage = '''
TO GET GET ARTIST SONG'S LYRICS : python3 lyrics.py ARTISTNAME SONGTITLE

IF ARTIST NAME OR SONG TITLE MORE THEN ONE WORD THEN SUBMIT COMMAND LINE ARGUMENT IN DOUBLE OR SINGLE QUOTE

FOR EXAMPLE IF YOU WANT TO GET EMINEM'S RAP GOD LYRICS : python3 lyrics.py eminem 'rap god'

AFTER EXECUTION lyrics.py WILL PRODUCE A FILE THAT CONTAIN YOUR REQUESTED LYRICS
'''

if(len(sys.argv) > 1):
    if(len(sys.argv) == 3):
        webpage = "https://genius.com"
        artist = str(sys.argv[1]).capitalize()
        artist = [mystring.replace(" ", "-") for mystring in artist]
        artist = "".join(artist)
        song = [mystring.replace(" ", "-") for mystring in str(sys.argv[2])]
        song = "".join(song)
        parameter = artist+"-"+song+"-lyrics"
        finaleAddress = webpage+"/"+parameter
        genius = requests.get(finaleAddress)
        pageContent = BeautifulSoup(genius.content,'html.parser')
        lyrics = pageContent.find(class_="lyrics")
        lyrics = pageContent.find("p").get_text()
        if(lyrics == '''
    Sorry, we didn\'t mean for that to happen!
  '''):
            print('''SORRY SONG NOT FOUND PLEASE CHECK ONE MORE TIME YOUR SONG TITLE AND ARTIST
IF SONG HAS A FEATURED ARTIST PLEASE PROVIDE THAT NAME AFTER MAIN ARTIST NAME IN COMMAND LINE\n''')
        else:
            f = open(parameter+".txt","w+")
            f.write(lyrics)
            print("SUCCESSFULLY LYRICS WRITTEN TO "+parameter+".txt FILE\n")
    else:
        print(useage)
else:
    print(useage)