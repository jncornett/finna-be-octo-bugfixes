#!/usr/bin/python

import os
import random
import subprocess

osascript = '''\
tell application "Finder"
	set desktop picture to POSIX file "%s"
end tell'''

PHOTO_DIRECTORY = ""
script = '{default = {ImageFilePath = "%s"; };}'

# Select a random photo from the photo directory
photos = [item for item in os.listdir(PHOTO_DIRECTORY) if item.endswith('.jpg')]
photo = random.choice(photos)

# Set background via osascript
subprocess.call(["osascript", "-e", osascript % (PHOTO_DIRECTORY + photo)])