#!/bin/bash


# Configure monitors
xrandr --output DP-1 --mode 1920x1080 --rate 60 --primary
xrandr --output HDMI-3 --mode 1920x1080 --rate 60 --left-of DP-1

# Set keyboard layout, just in case
setxkbmap -layout es

# Start composer
picom -b

# Set background
feh --bg-fill ~/Documents/wallpapers/ubuntu-magenta-blue-1920x1080.png

