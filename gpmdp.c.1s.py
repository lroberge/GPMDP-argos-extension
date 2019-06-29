#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Wnck', '3.0')

from gi.repository import Gtk, Wnck
import json
import math
import psutil
import os
import base64
import requests

#Replace this with the path to your GPMDP json_store folder
#It should be around the same place with the username changed
json_path = "/home/luke/.config/Google Play Music Desktop Player/json_store/playback.json"

#This function (and only this function) taken from https://github.com/Skillzore/argosSpotifyExtension
def isRunning(name):
	for proc in psutil.process_iter():
		if(proc.name() == name):
			return True

def isStopped():
	for win in screen.get_windows():
		if(win.get_name() == "Google Play Music Desktop Player"):
			return True

Gtk.init([])
screen = Wnck.Screen.get_default()
screen.force_update()

if(isRunning("Google Play Music Desktop Player") == None):
	print("")
	print("---")
	print("nothing to see")
	exit()

f = open(json_path, "r")
raw = f.read()
f.close()
playing = json.loads(raw)

if(isStopped()):
	print("Nothing playing | iconName=media-playback-stop")
	exit()

if(playing["song"]["title"] == None):
	print("GPMDP starting...")
	exit()

if(playing["song"]["albumArt"] != None):
	image = base64.b64encode(requests.get(playing["song"]["albumArt"]).content)

totalMin = math.floor(playing["time"]["total"] / 1000 / 60)
totalSec = math.floor((playing["time"]["total"] - (totalMin * 60 * 1000)) / 1000)
currentMin = math.floor(playing["time"]["current"] / 1000 / 60)
currentSec = math.floor((playing["time"]["current"] - (currentMin * 60 * 1000)) / 1000)
percent = math.floor(playing["time"]["current"] / playing["time"]["total"] * 100) * 2

nav = playing["song"]["title"] + " - " + playing["song"]["artist"] + "| iconName="
if(playing["playing"]):
	nav = nav + "media-playback-start"
else:
	nav = nav + "media-playback-pause"

print(nav)
print("---")
print(playing["song"]["title"] + "| size=24")
print("on " + playing["song"]["album"] + " by " + playing["song"]["artist"] +"| size=10")
if(image != None):
	print(" | image=" + str(image)[2:-1] + " imageWidth=200 imageHeight=200")
print(str(currentMin) + ":" + str(currentSec).zfill(2) + " / " + str(totalMin) + ":" + str(totalSec).zfill(2))
print("| image=iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+ip1sAAAAASUVORK5CYII= imageHeight=1 imageWidth=" + str(percent))

