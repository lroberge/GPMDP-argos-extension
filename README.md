# GPMDP-argos-extension
Puts information about the currently playing song in Google Play Music Desktop Player in a dropdown at the top of your screen using argos.  
It's supposed to refresh every second, but does so about every three (at least on my machine), indicating...something.  
This was made in an afternoon for "fun" and is pretty much my first experience with Python. It might not be terrible, but it's not particularly good.  


GPMDP: https://github.com/MarshallOfSound/Google-Play-Music-Desktop-Player-UNOFFICIAL-  
argos: https://github.com/p-e-w/argos

## How to install
Make sure [argos](https://github.com/p-e-w/argos) and python3 are installed, then put gpmdp.c.1s.py in ~/.config/argos.  
"Enable JSON API" should be ticked in GPMDP's Desktop Settings.  
If it's not working, make sure the .py file is marked as executable and that the home folder in the script is set correctly.
