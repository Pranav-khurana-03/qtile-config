#!/bin/sh


#Restore the wallpaper
nitrogen --restore

# Email Client
mailspring &


#Start the compositor, using experimental backends to use glx instead of xrendr
picom --experimental-backends & 


# Screensaver
xscreensaver -no-splash &
